# Motor

Bu bölüm, sabit kanatlı İHA itki sistemlerinde kullanılan fırçasız DC (BLDC) motorları tanımlar. Motorlar, elektriksel özellikleri, performans parametreleri ve fiziksel özellikleriyle belirtilir.

## Genel Bakış

Setuav Standardındaki motorlar, montajlarından bağımsız olarak tanımlanır. Motor tanımı, performans analizi, güç sistemi tasarımı ve ağırlık tahmini için gerekli tüm teknik özellikleri içerir.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Motorun benzersiz tanımlayıcısı (örn: "main_motor", "pusher_motor"). |
| **manufacturer** | `str` | Üretici adı (opsiyonel, örn: "Emax", "T-Motor"). |
| **model** | `str` | Model tanımlaması (opsiyonel, örn: "RS2205", "F60 PRO IV"). |

### Elektriksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **kv** | `RPM/V` | Motor hız sabiti (volt başına RPM). |
| **voltage_min** | `V` | Minimum çalışma voltajı. |
| **voltage_max** | `V` | Maksimum çalışma voltajı. |
| **current_max** | `A` | Maksimum sürekli akım değeri. |
| **resistance** | `Ω` | Faz-faz direnci (ohm). |
| **no_load_current** | `A` | Boştaki akım tüketimi (opsiyonel). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Montaj donanımı dahil motor ağırlığı. |
| **diameter** | `mm` | Statör çapı (opsiyonel). |
| **length** | `mm` | Mil hariç motor gövde uzunluğu (opsiyonel). |
| **shaft_diameter** | `mm` | Çıkış mili çapı (opsiyonel). |
| **shaft_length** | `mm` | Motor gövdesinden itibaren mil uzunluğu (opsiyonel). |
| **mounting_screw** | `str` | Montaj vida tipi (opsiyonel, örn: "M2", "M3"). |
| **mounting_spacing** | `str` | Montaj delik aralığı deseni (opsiyonel, örn: "16x16", "12x12", "19x19"). |

## Örnek Konfigürasyon

```yaml
motors:
  - tag: "main_motor"
    manufacturer: "Emax"
    model: "RS2205"
    kv: 2300
    voltage_min: 11.1
    voltage_max: 14.8
    current_max: 25
    resistance: 0.08
    no_load_current: 0.5
    mass: 28
    diameter: 28
    length: 31
    shaft_diameter: 5
    shaft_length: 12
    mounting_screw: "M3"
    mounting_spacing: "16x16"
  
  - tag: "pusher_motor"
    manufacturer: "T-Motor"
    model: "F60 PRO IV"
    kv: 1750
    voltage_min: 14.8
    voltage_max: 22.2
    current_max: 40
    resistance: 0.045
    mass: 62
    diameter: 28
    length: 37.3
```
