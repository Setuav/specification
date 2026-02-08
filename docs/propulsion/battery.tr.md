# Pil (Batarya)

Bu bölüm, İHA itki ve aviyonik sistemlerini besleyen pilleri tanımlar. Batarya elektriksel verileri **hücre seviyesinde** tanımlanır ve seri/paralel topoloji ile paket davranışı elde edilir.

## Genel Bakış

Setuav Standardında batarya elektriksel özellikleri hücre bazında tutulur ve aşağıdaki topoloji ile paket değerleri türetilir:

- `cells_series` (S)
- `cells_parallel` (P)

Bu yaklaşım, birbiriyle çelişen paket voltaj/kapasite girişlerini önler.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Pilin benzersiz tanımlayıcısı (örn: `main_battery`). |
| **manufacturer** | `str` | Üretici adı (opsiyonel). |
| **model** | `str` | Model adı (opsiyonel). |

### Hücre Seviyesi Elektriksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **chemistry** | `enum` | Hücre kimyası: `LiPo`, `LiHV`, `LiFe`, `Li-ion`, `NiMH`, `NiCd`. |
| **cells_series** | `int` | Seri hücre sayısı (S). |
| **cells_parallel** | `int` | Paralel hücre sayısı (P). |
| **cell_voltage_nominal** | `V` | Hücre başına nominal voltaj. |
| **cell_voltage_full** | `V` | Hücre başına tam dolu voltaj. |
| **cell_voltage_cutoff** | `V` | Hücre başına minimum güvenli voltaj. |
| **cell_capacity** | `mAh` | Hücre başına kapasite. |
| **cell_discharge_rate** | `C` | Hücre başına sürekli deşarj oranı. |
| **cell_discharge_burst** | `C` | Hücre başına anlık deşarj oranı (opsiyonel). |
| **cell_charge_rate** | `C` | Hücre başına maksimum şarj oranı (opsiyonel, varsayılan: 1C). |
| **cell_resistance** | `mΩ` | Hücre başına iç direnç (opsiyonel). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Batarya paket ağırlığı. |
| **dimensions** | `object` | Paket fiziksel boyutları. |
| **dimensions.length** | `mm` | Uzunluk. |
| **dimensions.width** | `mm` | Genişlik. |
| **dimensions.height** | `mm` | Yükseklik/kalınlık. |

### Yerleşim

Piller `placement` nesnesi ile airframe'e yerleştirilir:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **placement** | `object` | Pilin airframe'deki yerleşimi (opsiyonel). |
| **placement.position.x/y/z** | `mm` | Pilin `SETUAV_BODY` koordinat sistemindeki konumu. |
| **placement.rotation.x/y/z** | `deg` | Pil yönelimi (opsiyonel). |

## Türetilen Paket Değerleri (Bilgilendirme)

Aşağıdaki değerler analiz araçları tarafından türetilir, ana batarya alanı olarak saklanmaz:

- `pack_voltage_nominal = cells_series * cell_voltage_nominal`
- `pack_voltage_full = cells_series * cell_voltage_full`
- `pack_voltage_cutoff = cells_series * cell_voltage_cutoff`
- `pack_capacity = cells_parallel * cell_capacity`

## Örnek Konfigürasyon

```yaml
batteries:
  - tag: "main_battery"
    manufacturer: "Tattu"
    model: "R-Line LiHV"
    chemistry: "LiHV"
    cells_series: 4
    cells_parallel: 1
    cell_voltage_nominal: 3.8
    cell_voltage_full: 4.35
    cell_voltage_cutoff: 3.0
    cell_capacity: 1550
    cell_discharge_rate: 95
    cell_discharge_burst: 190
    cell_charge_rate: 5
    cell_resistance: 12
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
    model: "Graphene LiPo"
    chemistry: "LiPo"
    cells_series: 3
    cells_parallel: 1
    cell_voltage_nominal: 3.7
    cell_voltage_full: 4.2
    cell_voltage_cutoff: 3.0
    cell_capacity: 5000
    cell_discharge_rate: 45
    cell_discharge_burst: 90
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
