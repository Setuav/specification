# Analiz Koşulları

Bu bölüm, performans raporlarının hangi fiziksel ve çevresel şartlar altında elde edildiğini tanımlayan parametreleri içerir.

## Genel Bakış

Bir İHA'nın performansı (stall hızı, tırmanma oranı, statik marj vb.) büyük ölçüde ağırlık, ağırlık merkezi konumu ve atmosferik yoğunluğa bağlıdır. Bu nedenle, `conditions` bölümü her rapor için zorunlu bir bağlam sağlar.

## Fiziksel Koşullar

| Parametre | Birim | Zorunlu | Açıklama |
| :--- | :--- | :--- | :--- |
| **total_mass** | `g` | Evet | Analiz anındaki toplam uçuş ağırlığı. |
| **cg_position_x** | `mm` | Evet | Analiz anındaki Ağırlık Merkezi (CG) konumu (burun ucundan). |

## Atmosferik Koşullar

| Parametre | Birim | Varsayılan | Açıklama |
| :--- | :--- | :--- | :--- |
| **altitude_msl** | `m` | 0 | Analiz irtifası (Deniz seviyesinden yükseklik). |
| **temperature** | `C` | 15.0 | Ortam sıcaklığı. |
| **air_density** | `kg/m³` | 1.225 | Hava yoğunluğu. Eğer verilmezse irtifa ve sıcaklıktan standart atmosfer modeline göre hesaplanmalıdır. |

## Örnek Konfigürasyon

```yaml
conditions:
  total_mass: 2500       # 2.5 kg uçuş ağırlığı
  cg_position_x: 610.5   # 610.5mm CG konumu
  altitude_msl: 1000     # 1000m irtifa
  temperature: 10.0      # 10 derece sıcaklık
  air_density: 1.112     # 1000m'deki yaklaşık yoğunluk
```
