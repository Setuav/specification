# Kanat Geometrisi

Bu bölüm, kanatların parametrik modelini tanımlar. Kanat modeli; ana kanatları, yatay stabilizeleri ve dikey stabilizeleri temsil edebilecek kadar esnektir.

## Yapı: Profil ve Kesitler
Bu standartta bir kanat, tek bir geometrik blok değil; **İstasyonlar (Profiller)** ve bunları birbirine bağlayan **Segmentler (Kesitler)** serisinden oluşur.

1.  **İstasyon (Profil/Profile)**: Açıklık boyunca belirli bir noktadaki 2D kesiti tanımlar. **Profil (Airfoil)**, **Veter (Chord)** ve **Burulma (Twist)** verilerini içerir.
2.  **Segment (Kesit/Section)**: İki komşu istasyon arasındaki 3D geometriyi tanımlar. Bir sonraki istasyonun mevcut istasyona göre nasıl konumlandığını açıklayan **Açıklık (Span)**, **Ok Açısı (Sweep)** ve **V-Açı (Dihedral)** verilerini içerir.

## Koordinat Çerçevesi ve Yerleşim
Her kanadın **Kök Profili (Root Profile)**, `SETUAV_BODY` çerçeve başlangıcına (burun ucu) göre yerleştirilir.

- **Kök Ofseti (`x`, `y`, `z`)**: Kök veter hattının hücum kenarı konumu.
- **Simetri**: Aksine bir belirtim olmadıkça, kanatların XZ-düzlemi ($Y=0$) boyunca aynalandığı varsayılır.

## Parametreler
Bir kanat, bir kesitler (sections) listesiyle tanımlanır. İlk girdi **Kök Profili**ni, sonraki girdiler ise bir sonraki profile uzanan segmentleri tanımlar.

### İstasyon (Profil) Özellikleri
| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **Chord** | `mm` | Mevcut istasyondaki veter uzunluğu. |
| **Twist** | `deg` | X-eksenine göre mutlak hücum (incidence) açısı. |
| **Airfoil** | `ref` | Kanat profili referansı (NACA, DAT veya koordinat dosyası). |

### Segment (Kesit) Özellikleri (bir sonraki istasyona bağlanan kısım)
| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **Span** | `mm` | Segmentin açıklık yönündeki mesafesi (uzantısı). |
| **Sweep** | `deg` | Bu segment için %25 veter hattının arkaya doğru açısı. |
| **Dihedral** | `deg` | Bu segment için %25 veter hattının yukarı doğru açısı. |

## Kontrol Yüzeyleri
Kanatlar genellikle, kanat montajının belirli açıklık bölgelerine eşlenen Kanatçık (Aileron) veya Flap gibi kontrol yüzeylerini barındırır.

## Örnek (Kavramsal YAML)
```yaml
name: "Ana Kanat"
type: "wing"
geometry:
  root_offset: [500, 0, 0]
  mirror: true
  sections:
    - chord: 240
      twist: 2.0
      airfoil: "naca2412" # Kök İstasyonu
    - span: 400
      sweep: 0.0
      dihedral: 0.0
      chord: 240
      twist: 2.0
      airfoil: "naca2412" # İç Kanat Ucu
    - span: 400
      sweep: 5.0
      dihedral: 5.0
      chord: 180
      twist: -1.0
      airfoil: "naca0012" # Dış Kanat Ucu
```
