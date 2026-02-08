# İtki Genel Bakış

Setuav Standardında sabit kanatlı bir İHA'nın itki sistemi, itki üreten ve elektrik gücü sağlayan bileşenleri tanımlar. Bu, motorları, elektronik hız kontrolörlerini (ESC), pervane ve bataryaları içerir.

## Temel Kavramlar

İtki sistemi şu prensiplerle tasarlanmıştır:

- **Bileşen Bazlı Tanımlama**: Her itki bileşeni (motor, ESC, pervane, batarya) teknik özellikleriyle bağımsız olarak tanımlanır.
- **Performans Verileri**: Bileşenler, itki eğrileri, verimlilik haritalası ve güç tüketimi gibi performans özelliklerini içerir.
- **Entegrasyon Hazır**: Tüm bileşenler, uçak yapısına sorunsuz entegrasyon için montaj özellikleri ve elektriksel gereksinimleri içerir.

## Bileşen Türleri

İtki sistemi aşağıdaki bileşen kategorilerini içerir:

1. **Motor**: KV değeri, maksimum akım, direnç ve verimlilik verilerini içeren fırçasız DC motorlar.
2. **ESC (Elektronik Hız Kontrolörü)**: Motor hızını düzenleyen elektronik kontrolörler, akım limitleri, voltaj aralığı ve protokol desteğini içerir.
3. **Pervane**: Çap, hatve ve performans verileri (itki ve tork eğrileri) ile tanımlanan sabit hatveli pervaneler.
4. **Batarya**: Hücre seviyesi elektriksel veriler ve S/P topolojisi (`cells_series`, `cells_parallel`) ile tanımlanan batarya paketleri.

## Sistem Entegrasyonu

İtki bileşenleri İHA tasarımına şu şekilde entegre edilir:

- **Konumlandırma**: Motorlar, `SETUAV_BODY` koordinat sistemi kullanılarak uçak yapısında konumlandırılır (position_x, position_y, position_z).
- **Yönelim**: Motor itki vektörleri yönelim parametreleri (pitch_rotation, roll_rotation, yaw_rotation) kullanılarak tanımlanır.
- **Güç Sistemi**: Batarya yerleşimi ve kablolama özellikleri, doğru ağırlık dağılımı ve elektrik bağlantısını sağlar.
- **Performans Analizi**: Kombine itki verileri, itki-ağırlık hesaplamalarını, dayanıklılık tahminlerini ve görev planlamasını mümkün kılar.

## Birimler ve Standartlar

Tüm itki özellikleri SI birimlerini kullanır:

- Güç: Watt (W)
- Akım: Amper (A)
- Voltaj: Volt (V)
- Kütle: gram (g) veya kilogram (kg)
- İtki: Newton (N)
- Hız: RPM (dakikadaki devir sayısı)
- Kapasite: mAh, hücre başına (`cell_capacity`) tanımlanır
