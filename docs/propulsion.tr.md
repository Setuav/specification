# İtki (Propulsion) Sistemi

Bu bölüm; motorlar, pervaneler ve elektronik hız kontrolcüler (ESC) dahil olmak üzere itki sistemi bileşenlerini tanımlar.

## Modele Genel Bakış
İtki sistemi, fiziksel özelliklerin ve performans haritalarının bir kombinasyonu ile tanımlanır.

## Motor
Motorlar, fiziksel sabitleri ve performans verileriyle tanımlanır.

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **KV** | `RPM/V` | Motor hız sabiti. |
| **Kütle** | `g` | Motorun ağırlığı. |
| **İç Direnç** | `ohms` | Fazlar arası direnç. |
| **Boşta Akım** | `A` | Belirli bir voltajda sıfır torktaki akım. |

## Pervane
Pervaneler bir kütüphaneden referans alınır veya geometrileri ve performans katsayıları ($C_T$, $C_P$) ile tanımlanır.

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **Diameter** | `inch` | Pervane çapı. |
| **Pitch** | `inch` | Pervane hatvesi. |
| **Kanat Sayısı** | `int` | Pervane kanat sayısı. |

## Batarya
| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **Hücre Sayısı** | `S` | Serideki hücre sayısı. |
| **Kapasite** | `mAh` | Toplam kapasite. |
| **Gerilim** | `V` | Nominal voltaj. |

## Örnek (Kavramsal YAML)
```yaml
propulsion:
  motor:
    name: "T-Motor AT2814"
    kv: 900
    mass: 105
  propeller:
    name: "APC 12x6E"
    diameter: 12.0
    pitch: 6.0
  battery:
    cells: 4
    capacity: 5000
```
