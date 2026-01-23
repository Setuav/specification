# Setuav Standard — Giriş

## Amaç
Setuav Standard, bir İHA tasarımını araçtan bağımsız şekilde tanımlamak için kullanılan bir formattır.

Bu repo yalnızca:

- standart metni,
- JSON Schema’lar,
- YAML örnekler,
- doğrulama rehberi

içerir.

Plugin API’ler ve uygulamaya özgü ayrıntılar bu reponun kapsamı dışındadır.

## Kapsam
Setuav Standardı, **sabit kanatlı İHA** tasarımlarını hedefler ve tasarım yaşam döngüsünün tamamını kapsayan kapsamlı bir veri modeli sunar:

- **Geometri**: Gövde (fuselage), kanatlar, kuyruklar ve kontrol yüzeylerini içeren hava aracı bileşenlerinin parametrik tanımı.
- **Elektronik**: İtki sistemleri (motorlar, ESC'ler, pervaneler) ve güç sistemleri (piller) için teknik özellikler.
- **Üretim**: Fiziksel parçaların ağırlık, malzeme özellikleri ve montaj verileriyle eşleştirilmesi.
- **Performans**: Uçuş performans analizi, stabilite sonuçları ve görev simülasyon verilerinin depolanması için standart format.

## Kapsam dışı
Tasarım tanımına odaklanmak amacıyla, aşağıdaki alanlar kapsam dışı bırakılmıştır:

- **Döner Kanat**: Multirotor ve helikopter konfigürasyonları ve bunlara özgü parametreler (rotor diskleri, kolektif/çevrimsel hatve vb.).
- **Aviyonik İç Mantığı**: Detaylı kontrol yasaları, PID kazanımları veya otopilot yazılımına özgü kodlar.
- **Detaylı Yapısal Analiz**: Ham FEA ağ (mesh) verileri veya iç gerilme/zorlanma tensörleri (standart, yüksek seviyeli malzeme özellikleri ve kütle dağılımına odaklanır).
- **Operasyonel Veriler**: Bakım kayıtları, uçuş günlükleri, operatör lisansları ve anlık görev telemetri verileri.

## Temel İlkeler
Standart, birkaç temel ilke etrafında tasarlanmıştır:
- **Modülerlik**: Büyük tasarımlar daha küçük, tekrar kullanılabilir bileşen dosyalarına bölünebilir.
- **İnsan Tarafından Okunabilirlik**: YAML formatı, verilerin insanlar tarafından okunmasını ve düzenlenmesini kolaylaştırır.
- **Sıkı Doğrulama**: JSON Schema'lar, veri yapısı ve tipleri için net kurallar sağlar.
