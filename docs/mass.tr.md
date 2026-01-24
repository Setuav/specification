# Kütle ve Ek Parçalar

Bu bölüm, İHA bileşenleri için kütle bilgisinin nasıl belirtileceğini ve geometri veya itki sistemlerinde yakalanmayan ek parçaların nasıl takip edileceğini tanımlar.

## Genel Bakış

Setuav Standardı, kütle yönetimi için basit bir yaklaşım kullanır:

- **Geometri Bileşenleri**: Gövde ve kanatlar opsiyonel `mass` parametresine sahip olabilir (gram cinsinden)
- **İtki Bileşenleri**: Motorlar, ESC'ler, pervaneler ve piller `mass` parametresi içerir
- **Ek Parçalar**: Geometri ve itki dışındaki bileşenler (elektronikler, iniş takımı, vb.) kütle ve yerleşim bilgisiyle ayrı olarak belirtilir

## Geometri Kütlesi

Geometri bileşenleri (Fuselage, Wing) doğrudan kütle belirtebilir:

```yaml
airframe:
  fuselage:
    tag: "main_fuselage"
    mass: 250  # gram (opsiyonel)
    geometry:
      sections: ...
  
  wings:
    - tag: "main_wing"
      mass: 180  # kanat başına gram (opsiyonel)
      geometry:
        profiles: ...
```

**Not**: Bir kanadın bağlantısında `mirror: true` varsa, toplam kanat kütle katkısı 2 × mass olacaktır.

## Ek Parçalar

Geometri veya itki sistemlerinde temsil edilmeyen parçalar ek parçalar olarak belirtilir:

```yaml
additional_parts:
  - tag: "landing_gear"
    description: "Karbon fiber iniş takımı"
    mass: 120  # gram
    placement:  # opsiyonel, CG hesabı için
      position: {x: 500, y: 0, z: -50}
```

### Ek Parça Parametreleri

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **tag** | `str` | Benzersiz parça tanımlayıcısı. |
| **description** | `str` | İnsan tarafından okunabilir parça açıklaması (opsiyonel). |
| **mass** | `g` | Parça kütlesi. |
| **placement** | `object` | SETUAV_BODY çerçevesinde parça yerleşimi (opsiyonel). |
| **placement.position** | `object` | Pozisyon: {x, y, z} mm cinsinden. |

## Örnek Konfigürasyon

```yaml
setuav: '1.0'

airframe:
  fuselage:
    tag: "main_fuselage"
    mass: 250
    geometry:
      sections: ...
  
  wings:
    - tag: "main_wing"
      mass: 180
      geometry:
        profiles: ...

propulsion:
  motors:
    - tag: "main_motor"
      mass: 28
      # ... diğer motor parametreleri
  
  batteries:
    - tag: "main_battery"
      mass: 185
      # ... diğer pil parametreleri

additional_parts:
  - tag: "motor_mount"
    description: "3D baskı motor bağlantısı"
    mass: 12
    placement:
      position: {x: 0, y: 0, z: 0}
      
  - tag: "landing_gear"
    description: "Karbon fiber iniş takımı"
    mass: 120
    placement:
      position: {x: 500, y: 0, z: -50}
      
  - tag: "electronics_bay"
    description: "Uçuş kontrol cihazı, alıcı, GPS, kablolama"
    mass: 85
    placement:
      position: {x: 400, y: 0, z: -10}
```

## Ağırlık Merkezi Hesaplaması

Tüm bileşenler için yerleşim bilgisiyle, genel ağırlık merkezi hesaplanabilir:

$$
\vec{r}_{\text{CG}} = \frac{\sum_{i} m_i \cdot \vec{r}_i}{\sum_{i} m_i}
$$

Burada:

- $m_i$, $i$ bileşeninin kütlesi
- $\vec{r}_i$, SETUAV_BODY çerçevesinde $i$ bileşeninin pozisyon vektörü

**CG'ye katkıda bulunan bileşenler:**

- Gövde (eğer mass belirtilmişse)
- Kanatlar (kanat bağlantısından pozisyon, aynalama varsa mass × 2)
- Motorlar (placement'tan)
- ESC'ler (placement'tan)
- Piller (placement'tan)
- Ek parçalar (placement'tan)
- Pervaneler (motorlara monte, motor pozisyonunu kullan)

Bu hesaplama analiz araçları tarafından yapılmalıdır, spesifikasyonda saklanmamalıdır.
