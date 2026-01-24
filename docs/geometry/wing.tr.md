# Kanat Geometrisi

Bu bölüm, kanatların parametrik modelini tanımlar. Kanat modeli; ana kanatları, yatay stabilizeleri ve dikey stabilizeleri temsil edebilecek kadar esnektir.

## Yapı: Kesit Bazlı Profiller

Bu standartta bir kanat, belirli açıklık pozisyonlarındaki bir dizi **Kesit (Profil)** ile tanımlanır. Her kesit, o konumdaki kanat profili şeklini, veter uzunluğunu ve yönelimini tanımlar.

1. **Kesit (Profil)**: Açıklık boyunca belirli bir noktadaki 2D kesiti tanımlar. Konum, yönelim, geometrik özellikler (veter, kanat profili) ve rotasyonları içerir.
Kesitler, 3D kanat yüzeyini oluşturmak için parametrik yüzeylerle birbirine bağlanır.

## Koordinat Çerçevesi ve Yerleşim

Her kanadın istasyonları, **kanat-lokal koordinat sisteminde** tanımlanır:

- **Başlangıç**: Kanat bağlantı noktası (kök hücum kenarı)
- **X+**: Arka (firar kenarı yönüne doğru)
- **Y+**: Dışa doğru (kanat ucuna doğru)
- **Z+**: Yukarı (kanat referans düzlemine dik)

Tüm kanat daha sonra Wing Attachment parametreleri kullanılarak airframe içinde konumlandırılır (Wing Attachment bölümüne bakın).

- **Kök Ofseti**: Wing Attachment'ta belirtilir (gövde burnuna göre konum)
- **Simetri**: Kanatlar Wing Attachment'taki `mirror` parametresi kullanılarak aynalanır.

## Parametreler

Bir kanat, bir kesit (profil) listesi ile tanımlanır. Her kesit, konumunu ve yönelimini tamamen belirtir.

### Kesit Özellikleri

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **position** | `object` | Kesit pozisyonu (zorunlu). |
| **position.x** | `mm` | Kanat-lokal çerçevede boylamsal konum (tipik olarak ok açısı olmayan hücum kenarı için 0, pozitif = arka). |
| **position.y** | `mm` | Kanat kökünden açıklık yönünde konum (0 = kök, uca doğru artar). |
| **position.z** | `mm` | Kanat referans düzleminden dikey konum (0 = referans, pozitif = yukarı). |
| **chord** | `mm` | Bu istasyondaki veter uzunluğu. |
| **airfoil** | `str\|obj` | Kanat profili tanımı. Basit string formatı (örn: `"naca2412"`) veya detaylı obje formatı desteklenir. Detaylar için Kanat Profili Tanımı bölümüne bakın. |
| **rotation** | `object` | Kesit rotasyonu (opsiyonel). |
| **rotation.x** | `deg` | X-ekseni etrafında rotasyon (roll, opsiyonel, varsayılan: 0). |
| **rotation.y** | `deg` | Y-ekseni etrafında rotasyon (pitch/hücum/burulma açısı, opsiyonel, varsayılan: 0). |
| **rotation.z** | `deg` | Z-ekseni etrafında rotasyon (yaw, opsiyonel, varsayılan: 0). |

### Kanat Profili Tanımı

Kanat profilleri iki formatta tanımlanabilir:

**1. Basit Format (String)**:
Geriye uyumluluk ve basitlik için, NACA profilleri doğrudan string olarak belirtilebilir:

```yaml
airfoil: "naca2412"
```

**2. Detaylı Format (Object)**:
Daha fazla esneklik ve farklı kaynak türleri için obje formatı kullanılır:

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **type** | `enum` | Profil türü: `naca`, `file`, `coordinates`. |
| **code** | `str` | NACA kodu (`type: naca` için gerekli). Örn: `"2412"`, `"0012"`. |
| **path** | `str` | DAT dosya yolu (`type: file` için gerekli). Proje köküne göre göreli yol. |
| **points** | `array` | Koordinat dizisi (`type: coordinates` için gerekli). `[[x, y], ...]` formatında normalize edilmiş koordinatlar (0-1 arası). |

**Örnekler**:

```yaml
# NACA profili
airfoil:
  type: "naca"
  code: "2412"

# DAT dosyası
airfoil:
  type: "file"
  path: "profiles/custom_airfoil.dat"

# Koordinat tablosu
airfoil:
  type: "coordinates"
  points: [[1.0, 0.0], [0.95, 0.012], [0.90, 0.018], ...]
```

### Yüzey Oluşturma Parametreleri

Bu parametreler, kanat yüzeyini oluşturmak için komşu profillerin nasıl harmanlanacağını kontrol eder.

| Parametre | Tip | Varsayılan | Açıklama |
| :--- | :--- | :--- | :--- |
| **ruled** | `bool` | `false` | `false`: Düzgün yaklaşık yüzey. `true`: Çizgisel yüzey (profiller arası düz çizgiler). |
| **max_degree** | `int` | `3` | B-spline yaklaşımı için maksimum polinom derecesi. Geçerli aralık: `1-8`. Yüksek değerler daha düzgün eğrilere izin verir. |
| **continuity** | `enum` | `G2` | Hedef yüzey düzgünlüğü: `G0` (konum sürekliliği), `G1` (teğet sürekliliği), `G2` (eğrilik sürekliliği). |

## Kontrol Yüzeyleri

Kontrol yüzeyleri, kanat geometrisine açıklık boyunca belirli bölgelere eşlenen hareketli yüzeylerdir. Aileron, Flap, Elevator gibi yüzeyler bu şekilde tanımlanır.

### Kontrol Yüzeyi Parametreleri

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Kontrol yüzeyinin benzersiz tanımlayıcısı (örn: "left_aileron", "flap"). |
| **type** | `enum` | Kontrol yüzeyi türü: `aileron`, `flap`, `elevator`, `rudder`. |
| **span_start** | `mm` | Kontrol yüzeyinin başladığı açıklık pozisyonu (position_y koordinatına karşılık gelir). |
| **span_end** | `mm` | Kontrol yüzeyinin bittiği açıklık pozisyonu (position_y koordinatına karşılık gelir). |
| **chord** | `mm` | Kontrol yüzeyinin veter uzunluğu. Her station'da firar kenarından bu mesafe kadar ölçülür. |

**Not**: Menteşe hattı, kontrol yüzeyi başlangıcında (firar kenarından `chord` mm mesafede) implicit olarak tanımlanır.

### Örnek Kontrol Yüzeyi Tanımı

```yaml
control_surfaces:
  - tag: "left_aileron"
    type: "aileron"
    span_start: 500    # Kökten 500mm'de başlar
    span_end: 800      # Kökten 800mm'de biter
    chord: 60          # 60mm veter uzunluğu
  
  - tag: "flap"
    type: "flap"
    span_start: 100
    span_end: 450
    chord: 75
```

## Örnek Konfigürasyon

```yaml
tag: "main_wing"
type: "wing"
geometry:
  blending:
    ruled: false
    max_degree: 3
    continuity: "G2"
  
  profiles:
    - position:            # Hücum kenarında kök profili
        x: 0
        y: 0
        z: 0
      chord: 240
      rotation:
        y: 2.0
      airfoil: "naca2412"  # Basit format
    
    - position:            # Orta-açıklık profili
        x: 0
        y: 400
        z: 0
      chord: 240
      rotation:
        y: 2.0
      airfoil:              # Detaylı format
        type: "naca"
        code: "2412"
    
    - position:            # Uç profili (ok açılı ve V-açılı)
        x: 35
        y: 800
        z: 35
      chord: 180
      rotation:
        y: -1.0  # Washout
      airfoil:
        type: "naca"
        code: "0012"
  
  control_surfaces:
    - tag: "left_aileron"
      type: "aileron"
      span_start: 500
      span_end: 800
      chord: 60
    
    - tag: "flap"
      type: "flap"
      span_start: 100
      span_end: 450
      chord: 75
```
