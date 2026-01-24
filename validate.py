import argparse
import json
import yaml
import jsonschema
import os
from pathlib import Path
import sys

def load_schema_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_data(data_path):
    with open(data_path, 'r') as f:
        if data_path.endswith('.yaml') or data_path.endswith('.yml'):
            return yaml.safe_load(f)
        else:
            return json.load(f)

def create_store(schemas_root):
    store = {}
    for root, dirs, files in os.walk(schemas_root):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(root, file)
                try:
                    schema = load_schema_file(path)
                    if "$id" in schema:
                        store[schema["$id"]] = schema
                    
                    # Also allow resolving by relative path from the root if needed, 
                    # but typically $id is best.
                    # We can also add a file uri mapping
                    abs_path = os.path.abspath(path)
                    file_uri = Path(abs_path).as_uri()
                    store[file_uri] = schema
                except Exception as e:
                    print(f"Warning: could not load schema {path}: {e}")
    return store

def validate(data_path, schema_path, schemas_root):
    abs_schema_path = os.path.abspath(schema_path)
    
    try:
        schema = load_schema_file(abs_schema_path)
        data = load_data(data_path)
        store = create_store(schemas_root)
    except Exception as e:
        print(f"Error loading files: {e}")
        return False

    # Create a resolver that uses our store
    registry = store 
    # For older jsonschema, we use RefResolver with store
    # We set base_uri to the schema's URI so relative refs work if they are not in the store?
    # Or, simpler: Update the IDs in schemas to not use http if we don't want to.
    # But better is to just let the resolver find them in the store.
    
    schema_uri = schema.get("$id", Path(abs_schema_path).as_uri())

    try:
        resolver = jsonschema.RefResolver(base_uri=schema_uri, referrer=schema, store=store)
        
        jsonschema.validate(instance=data, schema=schema, resolver=resolver)
        print(f"Validation SUCCESS: {data_path} is valid against {schema_path}")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation FAILED: {data_path}")
        print(f"Message: {e.message}")
        print(f"Path: {e.json_path}")
        # print(f"Schema Path: {e.schema_path}")
        return False
    except Exception as e:
        print(f"An error occurred during validation: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Setuav Spec files against schemas.")
    parser.add_argument("data", help="Path to data file (YAML/JSON)")
    parser.add_argument("schema", help="Path to schema file (JSON)")
    parser.add_argument("--schemas-root", default="./schemas", help="Root directory of schemas to pre-load")
    
    args = parser.parse_args()
    success = validate(args.data, args.schema, args.schemas_root)
    if not success:
        sys.exit(1)
