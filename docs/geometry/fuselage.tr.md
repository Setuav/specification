# Gövde Geometrisi

Gövde modeli, İHA'nın ana gövdesini tanımlar. Tipik olarak, X-ekseni boyunca tanımlanan birkaç kesitin birbirine parametrik yüzeylerle bağlandığı bir istasyon bazlı yaklaşım kullanılır.

## Yapı: Kesitler ve Birleştirme

Gövde, X-ekseni boyunca belirli koordinatlarda tanımlanan bir dizi kesit (section) ile tanımlanır ve bu kesitler kontrollü interpolasyon ile birbirine bağlanır. Her kesit, konumunu, kesit şeklini (profile), ve oryantasyonunu içerir.

## Koordinat Çerçevesi

Gövde kesitleri `SETUAV_BODY` çerçevesinde tanımlanır.

- **X-ekseni**: Gövde boyunca mesafe (x=0 burun ucudur).
- **Y-Z düzlemi**: Kesitin bulunduğu düzlem.

## Parametreler

Gövde, kontrollü interpolasyon kullanılarak birbirine bağlanan bir dizi **kesit** (enine kesit) ile tanımlanır.

### Kesit Özellikleri

Her kesitin aşağıdaki özellikleri vardır:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **position_x** | `mm` | Burun ucundan boylamsal konum (zorunlu). |
| **position_y** | `mm` | XZ-düzleminden yanal ofset (opsiyonel, varsayılan: 0). Sabit kanatlı İHA'lar tipik olarak 0 kullanır (merkez hattı). |
| **position_z** | `mm` | XY-düzleminden dikey ofset (opsiyonel, varsayılan: 0). |
| **profile** | `object` | Kesit şekil tanımı (zorunlu). |
| **pitch** | `deg` | Kesit eğimi, X-eksenine göre (opsiyonel, varsayılan: 0). |
| **roll** | `deg` | Profil rotasyonu, X-ekseni etrafında (opsiyonel, varsayılan: 0). |

### Profil Tipleri

#### Circle

Çap ile tanımlanan dairesel kesit.

```yaml
profile:
  type: "circle"
  diameter: 80  # mm
```

#### Ellipse

Bağımsız genişlik ve yüksekliğe sahip eliptik kesit.

```yaml
profile:
  type: "ellipse"
  width: 100   # mm
  height: 120  # mm
```

#### Rectangle

Opsiyonel yuvarlatılmış köşelere sahip dikdörtgen kesit.

```yaml
profile:
  type: "rectangle"
  width: 100          # mm
  height: 120         # mm
  corner_radius: 10   # mm (opsiyonel, varsayılan: 0)
```

### Yüzey Birleştirme Parametreleri

Bu parametreler, kesitlerin nihai yüzeyi oluşturmak için nasıl harmanlanacağını kontrol eder.

| Parametre | Tip | Varsayılan | Açıklama |
| :--- | :--- | :--- | :--- |
| **ruled** | `bool` | `false` | `false`: Düzgün yaklaşık yüzey. `true`: Çizgisel yüzey (kesitler arası düz çizgiler). |
| **max_degree** | `int` | `3` | B-spline yaklaşımı için maksimum polinom derecesi. Geçerli aralık: `1-8`. Yüksek değerler daha düzgün eğrilere izin verir. |
| **continuity** | `enum` | `G2` | Hedef yüzey düzgünlüğü: `G0` (konum sürekliliği), `G1` (teğet sürekliliği), `G2` (eğrilik sürekliliği). |

**Determinizm Garantisi**: Aynı kesitler ve blend parametreleri verildiğinde, tüm uyumlu implementasyonlar verilen herhangi bir x pozisyonunda eşdeğer enine kesitlere sahip yüzeyler üretmelidir (±%0.1 tolerans dahilinde).

## Örnek Konfigürasyon

```yaml
tag: "main_fuselage"
type: "fuselage"
geometry:
  blending:
    ruled: false      # Düzgün yaklaşık yüzey
    max_degree: 3     # Kübik B-spline
  
  sections:
    - position_x: 0
      position_y: 0
      position_z: 0
      profile:
        type: "circle"  # Burun ucu
        diameter: 1 
    
    - position_x: 150
      position_y: 0
      position_z: 10     # Yükseltilmiş kokpit
      profile:
        type: "ellipse"
        width: 80
        height: 100
      pitch: 0.0
    
    - position_x: 600
      position_y: 0
      position_z: 0
      profile:
        type: "ellipse"
        width: 80
        height: 100
    
    - position_x: 1200
      position_y: 0
      position_z: 0
      profile:
        type: "circle"
        diameter: 20  # Kuyruk borusu
```
