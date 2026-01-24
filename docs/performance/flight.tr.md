# Uçuş Performansı

Bu modül, aracın uçuş zarfını (envelope) ve görev performansını tanımlayan metrikleri içerir.

## Hızlar (V-Speeds)

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **stall_speed** | `m/s` | Ağırlığı taşıyamadığı minimum hız (CL_max'ta). |
| **cruise_speed** | `m/s` | Verimli seyir hızı (genellikle L/D max civarı). |
| **max_speed** | `m/s` | Motor gücünün sürüklemeyi yenebildiği maksimum düz uçuş hızı. |

## Seyir Performansı

Seyir hızında (cruise_speed) beklenen değerler:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **power_required** | `W` | Seyir için gereken motor/pervane çıkış gücü. |
| **current_draw** | `A` | Bataryadan çekilen akım. |
| **endurance_hours** | `saat` | Toplam havada kalış süresi. |
| **range_km** | `km` | Toplam uçuş menzili. |

## Performans Eğrileri

Farklı uçuş hızları için hesaplanan güç ve itki gereksinimleri `curves` nesnesi altında diziler halinde sunulur. Bu veriler "Güç Gereksinimi vs Hız" grafikleri çizmek için kullanılır.

## Örnek Konfigürasyon

```yaml
flight:
  stall_speed: 12.0
  cruise_speed: 18.0
  max_speed: 32.0
  max_climb_rate: 6.5
  cruise_performance:
    power_required: 145
    current_draw: 6.5
    endurance_hours: 1.8
    range_km: 110
  curves:
    velocities: [10, 12, 14, 16, 18, 20, 25, 30]
    power_required: [200, 160, 140, 135, 145, 170, 250, 400]
    power_available: [600, 580, 560, 540, 520, 500, 450, 400]
    thrust_required: [15, 11, 9, 8, 8, 9, 12, 18]
    thrust_available: [40, 35, 30, 25, 20, 18, 15, 10]
```
