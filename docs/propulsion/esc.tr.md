# ESC (Elektronik Hız Kontrolörü)

Bu bölüm, İHA itki sistemlerinde motor hızını düzenlemek için kullanılan elektronik hız kontrolörlerini (ESC) tanımlar. ESC'ler, elektriksel özellikleri, iletişim protokolleri ve fiziksel özellikleriyle belirtilir.

## Genel Bakış

Setuav Standardındaki ESC'ler bağımsız olarak tanımlanır ve motorlar tarafından referans edilir. ESC tanımı, güç sistemi tasarımı ve ağırlık dağılımı için gerekli elektriksel özellikleri, protokol desteğini ve yerleşim bilgisini içerir.

## Parametreler

### Tanımlama

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | ESC'nin benzersiz tanımlayıcısı (örn: "main_esc", "pusher_esc"). |
| **manufacturer** | `str` | Üretici adı (opsiyonel, örn: "Hobbywing", "Castle Creations"). |
| **model** | `str` | Model tanımlaması (opsiyonel, örn: "XRotor 40A", "Phoenix Edge 80"). |

### Elektriksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **current_max** | `A` | Maksimum sürekli akım değeri. |
| **current_burst** | `A` | Maksimum anlık akım (opsiyonel, genellikle 10-30 saniye). |
| **voltage_min** | `V` | Minimum çalışma voltajı. |
| **voltage_max** | `V` | Maksimum çalışma voltajı. |
| **resistance** | `Ω` | İç direnç (opsiyonel). |
| **bec_voltage** | `V` | Batarya Eliminatör Devresi çıkış voltajı (opsiyonel, BEC yoksa 0). |
| **bec_current** | `A` | BEC maksimum çıkış akımı (opsiyonel). |

### İletişim

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **protocol** | `enum` | Kontrol protokolü (opsiyonel): `PWM`, `OneShot125`, `OneShot42`, `MultiShot`, `DShot150`, `DShot300`, `DShot600`, `DShot1200`. |
| **firmware** | `str` | Firmware tipi (opsiyonel, örn: "BLHeli_S", "BLHeli_32", "AM32"). |
| **telemetry** | `bool` | Telemetri desteği (opsiyonel, varsayılan: false). |

### Fiziksel Özellikler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **mass** | `g` | Kablolar dahil ESC ağırlığı. |
| **dimensions** | `object` | Fiziksel boyutlar (opsiyonel). |
| **dimensions.length** | `mm` | Uzunluk. |
| **dimensions.width** | `mm` | Genişlik. |
| **dimensions.height** | `mm` | Yükseklik/kalınlık. |

### Yerleşim

ESC'ler placement nesnesi kullanılarak airframe'de konumlandırılır:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **placement** | `object` | ESC'nin airframe'deki yerleşimi (opsiyonel). |
| **placement.position** | `object` | ESC'nin SETUAV_BODY çerçevesindeki pozisyonu. |
| **placement.position.x** | `mm` | Boylamsal pozisyon (burun ucundan mesafe). |
| **placement.position.y** | `mm` | Yanal pozisyon (0 = merkez hattı, pozitif = sağ). |
| **placement.position.z** | `mm` | Dikey pozisyon (pozitif = yukarı). |
| **placement.rotation** | `object` | ESC yönelimi. |
| **placement.rotation.x** | `deg` | X-ekseni etrafında rotasyon (roll, opsiyonel, varsayılan: 0). |
| **placement.rotation.y** | `deg` | Y-ekseni etrafında rotasyon (pitch, opsiyonel, varsayılan: 0). |
| **placement.rotation.z** | `deg` | Z-ekseni etrafında rotasyon (yaw, opsiyonel, varsayılan: 0). |

## Örnek Konfigürasyon

```yaml
escs:
  - tag: "main_esc"
    manufacturer: "Hobbywing"
    model: "XRotor 40A"
    current_max: 40
    current_burst: 55
    voltage_min: 7.4
    voltage_max: 25.2
    resistance: 0.003
    bec_voltage: 5.0
    bec_current: 3.0
    protocol: "DShot600"
    firmware: "BLHeli_32"
    telemetry: true
    mass: 12
    dimensions:
      length: 45
      width: 25
      height: 8
    placement:
      position:
        x: 50
        y: 0
        z: -20
      rotation:
        x: 0
        y: 0
        z: 0
  
  - tag: "pusher_esc"
    manufacturer: "Castle Creations"
    model: "Phoenix Edge 80"
    current_max: 80
    current_burst: 100
    voltage_min: 11.1
    voltage_max: 25.2
    protocol: "PWM"
    firmware: "Castle_Link"
    telemetry: true
    mass: 28
    placement:
      position:
        x: 1150
        y: 0
        z: 30
      rotation:
        x: 0
        y: 0
        z: 0
```
