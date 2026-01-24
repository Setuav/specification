# Geometri Genel Bakış

Setuav Standardında sabit kanatlı bir İHA'nın geometrisi, bağımsız ancak birbiriyle bağlantılı bileşenler kümesi aracılığıyla tanımlanır. Bu modüler yaklaşım, kanatların, gövdelerin ve diğer yapısal elemanların birleştirilmesiyle karmaşık uçak yapılarının oluşturulmasına olanak tanır.

## Temel Kavramlar

Geometri sistemi şu prensiplerle tasarlanmıştır:

- **Parametrik Tanımlama**: Statik 3D örgüleri (mesh) depolamak yerine, bunları oluşturmak için gereken parametreleri depoluyoruz.
- **İstasyon Bazlı Lofting**: Çoğu bileşen (kanatlar ve gövdeler), pürüzsüz yüzeyler oluşturmak için birbirine bağlanan (loft edilen) enine kesitler (istasyonlar) ile tanımlanır.
- **Referans Çerçevesi Tutarlılığı**: Tüm bileşenler `SETUAV_BODY` çerçevesine göre konumlandırılır.

## Bileşen Türleri

Aşağıdaki bölümlerde şunları inceleyeceğiz:

1. **[Gövde (Fuselage)](fuselage.md)**: Boylamsal eksen boyunca loft edilen parametrik enine kesitler (kesitler) kullanarak ana gövdeyi tanımlama.
2. **[Kanat (Wing)](wing.md)**: Mutlak konumlandırma ile kesit bazlı bir yaklaşım kullanarak taşıma yüzeylerini, stabilizörleri ve kontrol yüzeylerini tanımlama.
3. **[Kanat Yerleşimi (Wing Attachment)](wing_attachment.md)**: Kanatları gövde üzerinde konumlandırma ve yönlendirme, aerodinamik entegrasyon için otomatik fairing oluşturma dahil.

## Koordinat Entegrasyonu

Tüm bileşenler `SETUAV_BODY` referans çerçevesinde konumlandırılır (orijin burun ucunda, X+ arka, Y+ sağ, Z+ yukarı). Kanatlar lokal koordinat sistemleri kullanır ve daha sonra Kanat Yerleşimi parametreleri (position_x, position_y, position_z, pitch_rotation, roll_rotation, yaw_rotation) ile yerleştirilir. Bu, nihai modelin aerodinamik ve yapısal analize hazır, birleşik bir birim olmasını sağlar.
