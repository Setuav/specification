# Aerodinamik Performans

Bu modül, hava aracının aerodinamik karakteristiklerini tanımlayan sayısal verileri içerir.

## Parametreler

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **cl_max** | `-` | Maksimum kaldırma katsayısı (stall durumu). |
| **cl_max_alpha** | `deg` | Maksimum kaldırmanın elde edildiği hücum açısı. |
| **cd_min** | `-` | Minimum sürükleme katsayısı (genellikle sıfır kaldırmada). |
| **ld_max** | `-` | Maksimum süzülme oranı (L/D). |
| **ld_max_alpha** | `deg` | Maksimum süzülme oranının elde edildiği hücum açısı. |

## Referans Değerler

Katsayıların boyutsuzlaştırılmasında kullanılan referans değerler:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **span** | `mm` | Referans kanat açıklığı. |
| **area** | `mm²` | Referans kanat alanı. |
| **mean_chord** | `mm` | Ortalama aerodinamik veter (MAC). |
| **reynolds_number** | `-` | Analizin yapıldığı yaklaşık Reynolds sayısı. |

## Polarlar

Hücum açısına (alpha) bağlı aerodinamik katsayıların değişimi diziler halinde saklanır.

## Örnek Konfigürasyon

```yaml
aerodynamics:
  cl_max: 1.45
  # ...
  polars:
    alphas: [-5, 0, 5, 10, 15]
    cl_values: [-0.2, 0.4, 0.9, 1.3, 1.45]
    cd_values: [0.03, 0.025, 0.04, 0.08, 0.15]
    ld_values: [-6.6, 16.0, 22.5, 16.25, 9.6]
```
