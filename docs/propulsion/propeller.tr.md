# Pervane

İHA itki sistemleri için sabit hatveli pervane spesifikasyonu.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Pervanenin benzersiz tanımlayıcısı (örn: "main_prop", "pusher_prop"). |
| **manufacturer** | `str` | Üretici adı (opsiyonel, örn: "APC", "GemFan"). |
| **model** | `str` | Model tanımlaması (opsiyonel, örn: "10x4.5MR", "10x7E"). |

### Geometrik Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **diameter** | `inç` | Pervane çapı (uçtan uca). |
| **pitch** | `inç` | Pervane hatvesi (devir başına teorik ilerleme). |
| **blade_count** | `int` | Kanat sayısı. |
| **direction** | `enum` | Dönüş yönü: `CW` (saat yönü) veya `CCW` (saat yönü tersi) arkadan bakıldığında. |
| **hub_diameter** | `mm` | Göbek çapı (opsiyonel). |
| **hub_thickness** | `mm` | Göbek kalınlığı (opsiyonel). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Pervane ağırlığı. |
| **material** | `str` | Malzeme tipi (opsiyonel, örn: "Carbon Fiber", "Plastic", "Wood"). |

## Örnek Yapılandırma

```yaml
propellers:
  - tag: "main_prop"
    manufacturer: "APC"
    model: "10x4.5MR"
    diameter: 10.0
    pitch: 4.5
    blade_count: 2
    direction: "CW"
    mass: 12
    material: "Plastic"

  - tag: "pusher_prop"
    manufacturer: "GemFan"
    model: "10x7"
    diameter: 10.0
    pitch: 7.0
    blade_count: 2
    direction: "CCW"
    mass: 15
    material: "Carbon Fiber"
    hub_diameter: 8
    hub_thickness: 6
```
