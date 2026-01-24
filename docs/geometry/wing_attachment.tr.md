# Kanat Yerleşimi

Bu bölüm, kanatların gövdeye nasıl bağlandığını, konumlarını, yönelimlerini ve opsiyonel aerodinamik fairing'lerini tanımlar.

## Genel Bakış

Bir **Kanat Yerleşimi (Wing Attachment)**, kanat geometrisini airframe içindeki konumuyla birleştirir. Kanat kökünün gövdeye nerede bağlandığını ve nasıl yönlendirildiğini belirtir.

## Koordinat Sistemi

Tüm yerleşim koordinatları `SETUAV_BODY` çerçevesine göre tanımlanır (başlangıç noktası gövde burun ucu):

- **X+**: Arka (kuyruk yönüne)
- **Y+**: Sağ (starboard)
- **Z+**: Yukarı

## Yerleşim Parametreleri

### Konum

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **position** | `object` | Kanat yerleşimi pozisyonu (zorunlu). |
| **position.x** | `mm` | Gövde boyunca boylamsal konum (burun ucundan mesafe). |
| **position.y** | `mm` | Merkez hattından yanal ofset. Genellikle V-kuyruk veya asimetrik konfigürasyonlar için sıfırdan farklıdır. |
| **position.z** | `mm` | Gövde referans hattından dikey ofset. Pozitif değerler kanadı yukarı kaldırır. |

### Yönelim

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **rotation** | `object` | Kanat yerleşimi rotasyonu (opsiyonel). |
| **rotation.x** | `deg` | X-ekseni (boylamsal eksen, roll) etrafında rotasyon. V-açı veya V-kuyruk konfigürasyonları için kullanılır. Pozitif rotasyon sağ kanadı yukarı doğru eğer (opsiyonel, varsayılan: 0). |
| **rotation.y** | `deg` | Y-ekseni (yanal eksen, pitch) etrafında rotasyon. Kanadın hücum açısını ayarlar (opsiyonel, varsayılan: 0). |
| **rotation.z** | `deg` | Z-ekseni (dikey eksen, yaw) etrafında rotasyon. Tüm kanat için global bir ok açısı etkisi yaratır (opsiyonel, varsayılan: 0). |

### Simetri

| Parametre | Tip | Açıklama |
| :--- | :--- | :--- |
| **mirror** | `bool` | `true` ise, kanat XZ-düzlemi (Y=0) boyunca aynalanararak simetrik bir çift oluşturulur. `false` ise, sadece tek bir kanat yerleştirilir. |

## Kanat-Gövde Bağlantısı (Fairing)

Bir **fairing**, kanat kökünü gövdeye yumuşak bir şekilde harmanlayan aerodinamik bir geçiş yüzeyidir ve müdahale sürtünmesini (interference drag) azaltır.

### Fairing Parametreleri

| Parametre | Tip | Varsayılan | Açıklama |
| :--- | :--- | :--- | :--- |
| **scale** | `float` | `1.2` | Fairing profili için tekdüze ölçekleme faktörü. Aralık: 1.1-1.4. |
| **leading_curve** | `float` | `0.3` | Hücum kenarı eğriliği: pozitif = dışbükey (dışa eğri), negatif = içbükey (içe eğri), 0 = doğrusal. Aralık: -1.0 ile 1.0. |
| **trailing_curve** | `float` | `-0.2` | Firar kenarı eğriliği: pozitif = dışbükey (dışa eğri), negatif = içbükey (içe eğri), 0 = doğrusal. Aralık: -1.0 ile 1.0. |
| **continuity** | `str` | `G2` | Yüzey sürekliliği: `G0` (konumsal), `G1` (teğet), veya `G2` (eğrilik). |

### Fairing Geometrisi

Fairing otomatik olarak şu şekilde oluşturulur:

1. Kanat kök profili çıkarılır
2. `scale` faktörü ile ölçeklenir ve gövde ile kesişecek şekilde konumlandırılır
3. Hücum ve firar kenarlarında dışbükey (dışa) veya içbükey (içe) geçişler oluşturmak için eğrilik kontrolü uygulanır
4. Belirtilen süreklilik ile profiller arası loft oluşturulur
5. Sonuç gövde yüzeyine göre kesilir

**Eğrilik Kontrolü**:

- **Pozitif eğri** (0 ile 1.0): Dışbükey geçiş, dışa eğri - girişim direncini azaltır
- **Negatif eğri** (-1.0 ile 0): İçbükey geçiş, içe eğri - daha yumuşak entegrasyon sağlar
- **Sıfır eğri**: Doğrusal geçiş

Tipik olarak, hücum kenarları hafif pozitif eğri (dışbükey) kullanırken, firar kenarları optimal aerodinamik için hafif negatif eğri (içbükey) kullanır.

## Örnek Konfigürasyon

```yaml
wings:
  - tag: "main_wing"
    attachment:
      position:
        x: 450    # Burundan 450mm
        y: 0      # Merkez hattı
        z: 50     # Referanstan 50mm yukarı
      rotation:
        x: 2.0    # 2° V-açı
        y: 0      # Hücum açısı ofseti yok
        z: 0      # Global ok açısı yok
      mirror: true       # Simetrik çift
      fairing:
        scale: 1.2
        leading_curve: 0.3
        trailing_curve: -0.2
        continuity: "G2"
    
    geometry:
      blending:
        ruled: false
        max_degree: 3
        continuity: "G2"
      profiles:
        - position:
            x: 0
            y: 0
            z: 0
          chord: 240
          rotation:
            y: 2.0
          airfoil: "naca2412"
        # Ek profiller...

  - tag: "horizontal_stabilizer"
    attachment:
      position:
        x: 1200   # Kuyruk yakını
        y: 0
        z: 120
      rotation:
        x: 0
        y: 0
        z: 0
      mirror: true       # Simetrik çift
      fairing:
        scale: 1.15
        leading_curve: 0.2
        trailing_curve: -0.15
        continuity: "G1"
    
    geometry:
      blending:
        ruled: false
        max_degree: 3
        continuity: "G2"
      profiles:
        - position:
            x: 0
            y: 0
            z: 0
          chord: 150
          rotation:
            y: 0
          airfoil: "naca0012"
        # Ek profiller...
```
