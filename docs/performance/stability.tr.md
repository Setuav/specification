# Stabilite

Bu modül, hava aracının statik ve dinamik kararlılık özelliklerini tanımlayan **sayısal türevleri** ve denge noktalarını içerir.

## Boylamsal Stabilite

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **neutral_point_x** | `mm` | Nötr noktanın (aerodinamik merkez) burna göre konumu. |
| **static_margin** | `%` | Statik marj ((X_np - X_cg) / MAC). Pozitif değerler kararlı, negatif değerler kararsızdır. |
| **trim_alpha** | `deg` | Denge durumundaki (pitch moment = 0) hücum açısı. |
| **trim_elevator** | `deg` | Denge durumundaki elevatör açısı. |

## Stabilite Türevleri

Bu katsayılar, aracın bozucu etkilere (alfa veya beta açısı değişimleri) karşı verdiği tepkiyi belirler.

| Türev | Tanım | Anlamı | İstenen İşaret |
| :--- | :--- | :--- | :--- |
| **cm_alpha** | `dCm/dα` | Yunuslama momentinin alfa ile değişimi. (Pitch stiffness) | Negatif (< 0) |
| **cn_beta** | `dCn/dβ` | Sapma momentinin beta ile değişimi. (Directional stability - Weathercock) | Pozitif (> 0) |
| **cl_beta** | `dCl/dβ` | Yuvarlanma momentinin beta ile değişimi. (Dihedral effect) | Negatif (< 0) |

## Örnek Konfigürasyon

```yaml
stability:
  static_margin: 15.5
  neutral_point_x: 650.0
  derivatives:
    cm_alpha: -0.85
    cn_beta: 0.12
    cl_beta: -0.05
```
