# Gövde Geometrisi

Gövde modeli, İHA'nın ana yapısal gövdelerini tanımlar. Gövde, bir veya daha fazla "segment" (parça) halinde tanımlanır ve her segment bir dizi kesitin birbirine bağlanmasıyla oluşur.

## Yapı: Segmentler ve Loftlar

Gövde yapısı modülerdir. Tek bir gövde tanımı altında birden fazla "Segment" (bölüm) tanımlanabilir. Örneğin bir gövde "Burun Konisi", "Ana Tüp" ve "Motor Kulesi" olarak üç ayrı segmentten oluşabilir.

Her segment, X-ekseni boyunca (veya uzayda herhangi bir doğrultuda) tanımlanan bir dizi kesit (section) içerir ve bu kesitler kontrollü interpolasyon (loft) ile birbirine bağlanır.

## Koordinat Çerçevesi

Gövde segmentleri ve kesitleri `SETUAV_BODY` çerçevesinde tanımlanır.

- **X-ekseni**: Boylamsal eksen.
- **Y-Z düzlemi**: Kesitin bulunduğu düzlem.

## Parametreler

### Tanımlama ve Kütle

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Gövde için benzersiz tanımlayıcı (örn: "main_fuselage"). |
| **mass** | `g` | Toplam gövde kütlesi. |

### Geometri: Segmentler

Gövde geometrisi, `segments` dizisi altında tanımlanan parçaların toplamıdır. Her segmentin aşağıdaki özellikleri vardır:

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Segmente özgü etiket (örn: "nose_cone"). |
| **sections** | `list` | Segmenti oluşturan kesitlerin listesi (en az 2 adet). |
| **blending** | `object` | Bu segmente özel yüzey oluşturma parametreleri (opsiyonel). |

### Kesit Özellikleri

Her kesitin aşağıdaki özellikleri vardır:

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **position** | `object` | Kesit pozisyonu (zorunlu). |
| **position.x** | `mm` | Burun ucundan boylamsal konum. |
| **position.y** | `mm` | XZ-düzleminden yanal ofset (opsiyonel, varsayılan: 0). |
| **position.z** | `mm` | XY-düzleminden dikey ofset (opsiyonel, varsayılan: 0). |
| **profile** | `object` | Kesit şekil tanımı (zorunlu). |
| **pitch** | `deg` | Kesit eğimi, Y-ekseni etrafında (opsiyonel, varsayılan: 0). |
| **roll** | `deg` | Profil rotasyonu, X-ekseni etrafında (opsiyonel, varsayılan: 0). |

## Profil Tipleri

`sections` altındaki her kesit belirli bir profile sahip olmalıdır.

#### Circle (Daire)
```yaml
profile: {type: "circle", diameter: 80}
```

#### Ellipse (Elips)
```yaml
profile: {type: "ellipse", width: 100, height: 120}
```

#### Rectangle (Dikdörtgen)
```yaml
# Opsiyonel 'corner_radius' ile yuvarlatılabilir
profile: {type: "rectangle", width: 100, height: 120, corner_radius: 10}
```

## Yüzey Birleştirme (Blending)

Bu parametreler, segment içindeki kesitlerin nasıl birbirine bağlanacağını kontrol eder.

| Parametre | Varsayılan | Açıklama |
| :--- | :--- | :--- |
| **ruled** | `false` | `true` ise kesitler arası düz çizgilerle (cetvel yüzey) bağlanır. |
| **max_degree** | `3` | B-spline yüzeyin derecesi (1-8 arası). |
| **continuity** | `G2` | Yüzey süreklilik hedefi: `G0`, `G1`, `G2`. |

## Örnek Konfigürasyon

Bu örnek, bir Skywalker gövdesini iki segment halinde tanımlar: Ana tüp ve motor kulesi.

```yaml
tag: "skywalker_X8"
mass: 450
type: "fuselage"
geometry:
  segments:
    # 1. Segment: Ana Gövde Hattı
    - tag: "main_body"
      blending: {ruled: false}
      sections:
        - {position: {x: 0}, profile: {type: "circle", diameter: 5}}  # Sivri burun
        - {position: {x: 200}, profile: {type: "ellipse", width: 150, height: 90}} # Geniş gövde
        - {position: {x: 800}, profile: {type: "circle", diameter: 20}} # İnce kuyruk

    # 2. Segment: Motor Kulesi (Gövdenin üstünden çıkar)
    - tag: "motor_tower"
      blending: {ruled: true}
      sections:
        - {position: {x: 600, z: 50}, profile: {type: "ellipse", width: 40, height: 80}} # Kule tabanı
        - {position: {x: 650, z: 120}, profile: {type: "circle", diameter: 40}} # Firewall
```
