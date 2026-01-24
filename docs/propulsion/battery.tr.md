# Pil (Batarya)

Bu bölüm, İHA itki ve aviyonik sistemlerini beslemek için kullanılan pilleri tanımlar. Piller, elektriksel özellikleri, kimya tipi ve fiziksel özellikleriyle belirtilir.

## Genel Bakış

Setuav Standardındaki piller, elektriksel özellikleri ve yerleşim bilgileriyle bağımsız olarak tanımlanır. Pil tanımı, güç sistemi tasarımı ve ağırlık dağılımı için gerekli kapasite, voltaj özellikleri, deşarj kabiliyetleri ve fiziksel özellikleri içerir.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Pilin benzersiz tanımlayıcısı (örn: "main_battery", "aux_battery"). |
| **manufacturer** | `str` | Üretici adı (opsiyonel, örn: "Tattu", "Turnigy", "GensAce"). |
| **model** | `str` | Model tanımlaması (opsiyonel, örn: "R-Line 4S 1550mAh", "Graphene 3S 5000mAh"). |

### Elektriksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **chemistry** | `enum` | Pil kimyası: `LiPo`, `LiHV`, `LiFe`, `Li-ion`, `NiMH`, `NiCd`. |
| **cells** | `int` | Seri bağlı hücre sayısı (örn: 3S için 3, 4S için 4). |
| **voltage_nominal** | `V` | Nominal voltaj (LiPo için tipik olarak hücre × 3.7V, LiHV için hücre × 3.8V). |
| **voltage_full** | `V` | Tam şarj voltajı (LiPo için tipik olarak hücre × 4.2V, LiHV için hücre × 4.35V). |
| **voltage_cutoff** | `V` | Minimum güvenli deşarj voltajı (LiPo için tipik olarak hücre × 3.0V). |
| **capacity** | `mAh` | Miliamper-saat cinsinden pil kapasitesi. |
| **discharge_rate** | `C` | Maksimum sürekli deşarj oranı (örn: 75C için 75). |
| **discharge_burst** | `C` | Maksimum anlık deşarj oranı (opsiyonel, genellikle 10-30 saniye). |
| **charge_rate** | `C` | Maksimum şarj oranı (opsiyonel, varsayılan: 1C). |
| **resistance** | `mΩ` | İç direnç (opsiyonel). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Pil ağırlığı. |
| **dimensions** | `object` | Fiziksel boyutlar. |
| **dimensions.length** | `mm` | Uzunluk. |
| **dimensions.width** | `mm` | Genişlik. |
| **dimensions.height** | `mm` | Yükseklik/kalınlık. |

### Yerleşim

Piller placement nesnesi kullanılarak airframe'de konumlandırılır:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **placement** | `object` | Pilin airframe'deki yerleşimi (opsiyonel). |
| **placement.position** | `object` | Pilin SETUAV_BODY çerçevesindeki pozisyonu. |
| **placement.position.x** | `mm` | Boylamsal pozisyon (burun ucundan mesafe). |
| **placement.position.y** | `mm` | Yanal pozisyon (0 = merkez hattı, pozitif = sağ). |
| **placement.position.z** | `mm` | Dikey pozisyon (pozitif = yukarı). |
| **placement.rotation** | `object` | Pil yönelimi. |
| **placement.rotation.x** | `deg` | X-ekseni etrafında rotasyon (roll, opsiyonel, varsayılan: 0). |
| **placement.rotation.y** | `deg` | Y-ekseni etrafında rotasyon (pitch, opsiyonel, varsayılan: 0). |
| **placement.rotation.z** | `deg` | Z-ekseni etrafında rotasyon (yaw, opsiyonel, varsayılan: 0). |

## Örnek Konfigürasyon

```yaml
batteries:
  - tag: "main_battery"
    manufacturer: "Tattu"
    model: "R-Line 4S 1550mAh"
    chemistry: "LiHV"
    cells: 4
    voltage_nominal: 15.2
    voltage_full: 17.4
    voltage_cutoff: 12.0
    capacity: 1550
    discharge_rate: 95
    discharge_burst: 190
    charge_rate: 5
    resistance: 12
    mass: 185
    dimensions:
      length: 78
      width: 36
      height: 36
    placement:
      position:
        x: 350
        y: 0
        z: -15
      rotation:
        x: 0
        y: 0
        z: 0
  
  - tag: "long_range_battery"
    manufacturer: "Turnigy"
    model: "Graphene 3S 5000mAh"
    chemistry: "LiPo"
    cells: 3
    voltage_nominal: 11.1
    voltage_full: 12.6
    voltage_cutoff: 9.0
    capacity: 5000
    discharge_rate: 45
    discharge_burst: 90
    mass: 382
    dimensions:
      length: 138
      width: 43
      height: 29
    placement:
      position:
        x: 420
        y: 0
        z: -25
      rotation:
        x: 0
        y: 0
        z: 0
```
