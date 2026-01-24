# Pervane

Bu bölüm, İHA itki sistemlerinde kullanılan sabit hatveli pervaneleri tanımlar. Pervaneler, geometrik özellikleri ve performans karakteristikleriyle belirtilir.

## Genel Bakış

Setuav Standardındaki pervaneler bağımsız olarak tanımlanır ve motorlar tarafından referans edilir. Pervane tanımı, performans analizi ve uyumluluk doğrulaması için gerekli geometrik özellikleri içerir.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Pervanenin benzersiz tanımlayıcısı (örn: "main_prop", "pusher_prop"). |
| **manufacturer** | `str` | Üretici adı (opsiyonel, örn: "APC", "Graupner"). |
| **model** | `str` | Model tanımlaması (opsiyonel, örn: "9x4.5", "10x7E"). |

### Geometrik Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **diameter** | `mm` | Pervane çapı (uçtan uca). |
| **pitch** | `mm` | Pervane hatvesi (devir başına teorik ilerleme). |
| **blade_count** | `int` | Kanat sayısı (genellikle 2, 3 veya 4). |
| **direction** | `enum` | Dönüş yönü: `CW` (saat yönü) veya `CCW` (saat yönü tersi) arkadan bakıldığında. |
| **hub_diameter** | `mm` | Göbek çapı (opsiyonel). |
| **hub_thickness** | `mm` | Göbek kalınlığı (opsiyonel). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Pervane ağırlığı. |
| **material** | `str` | Malzeme tipi (opsiyonel, örn: "carbon_fiber", "nylon", "wood"). |

### Performans Verileri

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **thrust_data** | `array` | İtki eğrisi veri noktaları (opsiyonel). `{rpm, thrust_n, torque_nm, power_w}` nesnelerinden oluşan dizi. |
| **efficiency_data** | `array` | Verimlilik veri noktaları (opsiyonel). `{velocity_ms, efficiency, advance_ratio}` nesnelerinden oluşan dizi. |

#### İtki Verisi Yapısı

Her itki veri noktası şunları içerir:

| Alan | Birim | Açıklama |
| :--- | :--- | :--- |
| **rpm** | `RPM` | Dönüş hızı. |
| **thrust_n** | `N` | Üretilen itki kuvveti. |
| **torque_nm** | `Nm` | Gerekli tork. |
| **power_w** | `W` | Güç tüketimi. |

#### Verimlilik Verisi Yapısı

Her verimlilik veri noktası şunları içerir:

| Alan | Birim | Açıklama |
| :--- | :--- | :--- |
| **velocity_ms** | `m/s` | Uçuş hızı. |
| **efficiency** | `-` | İtki verimliliği (0-1). |
| **advance_ratio** | `-` | İlerleme oranı (J = V / (n * D)). |

## Pervane Montajı

Pervaneler motorlara monte edilir ve bağımsız yerleşime sahip değildir. Pervane pozisyonu ve yönelimi, bağlı olduğu motorun placement bilgisi tarafından belirlenir.

## Örnek Konfigürasyon

```yaml
propellers:
  - tag: "main_prop"
    manufacturer: "APC"
    model: "9x4.5"
    diameter: 228.6  # 9 inç = 228.6mm
    pitch: 114.3     # 4.5 inç = 114.3mm
    blade_count: 2
    direction: "CW"
    mass: 8
    material: "nylon"
  
  - tag: "pusher_prop"
    manufacturer: "Graupner"
    model: "10x7E"
    diameter: 254
    pitch: 177.8
    blade_count: 2
    direction: "CCW"
    mass: 12
    material: "carbon_fiber"
    hub_diameter: 8
    hub_thickness: 6
  
  - tag: "efficiency_prop"
    manufacturer: "APC"
    model: "11x5.5E"
    diameter: 279.4
    pitch: 139.7
    blade_count: 2
    direction: "CW"
    mass: 15
    material: "carbon_fiber"
    thrust_data:
      - rpm: 5000
        thrust_n: 2.5
        torque_nm: 0.08
        power_w: 41.9
      - rpm: 6000
        thrust_n: 3.6
        torque_nm: 0.11
        power_w: 69.1
      - rpm: 7000
        thrust_n: 4.9
        torque_nm: 0.15
        power_w: 110.0
```
