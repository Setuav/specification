# Gövde (Fuselage) Geometrisi

Gövde modeli, İHA'nın ana gövdesini tanımlar. Tipik olarak, X-ekseni boyunca tanımlanan birkaç kesitin birbirine bağlandığı (loft edildiği) bir istasyon bazlı yaklaşım kullanılır.

## Yapı: İstasyonlar ve Lofting
Gövde, belirli X-koordinatlarında yer alan bir dizi **İstasyon** ile tanımlanır.

1.  **İstasyon**: Belirli bir boylamsal konumdaki kesit.
2.  **Kesit (Cross-Section)**: Basit bir şekil (Daire, Kare, Yuvarlatılmış Dikdörtgen) veya karmaşık parametrik bir eğri olarak tanımlanabilir.

## Koordinat Çerçevesi
Gövde istasyonları `SETUAV_BODY` çerçevesinde tanımlanır.
- **X-ekseni**: Gövde boyunca mesafe (0 burun ucudur).
- **Y-Z düzlemi**: Kesitin bulunduğu düzlem.

## Parametreler
Şu anda standart, gövde için **Parametrik Lofting** yöntemini desteklemektedir.

### İstasyon Özellikleri
| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **x** | `mm` | Burun ucundan olan mesafe. |
| **width** | `mm` | Bu istasyondaki maksimum genişlik. |
| **height** | `mm` | Bu istasyondaki maksimum yükseklik. |
| **shape** | `enum` | Kesit tipi (`circle`, `ellipse`, `rectangle`, `box`). |
| **offset_z**| `mm` | Kesit merkezinin merkez hattından dikey ofseti. |

## Örnek (Kavramsal YAML)
```yaml
name: "Ana Gövde"
type: "fuselage"
geometry:
  stations:
    - x: 0
      width: 0
      height: 0
      shape: "circle" # Burun ucu
    - x: 150
      width: 80
      height: 100
      shape: "ellipse" # Kokpit bölgesi
    - x: 600
      width: 80
      height: 100
      shape: "ellipse" # Faydalı yük bölgesi sonu
    - x: 1200
      width: 20
      height: 20
      shape: "circle" # Kuyruk borusu çıkışı
```
