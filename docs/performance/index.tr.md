# Performans ve Analiz Raporları

Setuav Standardı, sadece İHA tasarımını değil, bu tasarımın analiz sonuçlarını saklamak ve paylaşmak için de bir yapı sunar. Bu bölüm, performans raporlarının nasıl yapılandırıldığını açıklar.

## Genel Bakış

Bir tasarım dosyasından (`design.yaml`) farklı olarak, performans raporları (`report.yaml`), bir analiz aracı veya test süreci tarafından üretilen **çıktıları** temsil eder. Bu ayrım, tasarım verileri ile sonuç verilerinin yaşam döngülerini birbirinden ayırır.

## Rapor Yapısı

Bir Setuav performans raporu (`report.json` şeması), beş ana bileşenden oluşur:

1.  **Analiz Koşulları (`conditions`)**: Analizin yapıldığı fiziksel (kütle, CG) ve atmosferik (irtifa, sıcaklık) ortam.
2.  **Aerodinamik (`aerodynamics`)**: Temel aerodinamik katsayılar ve polarlar.

4.  **Uçuş Performansı (`flight`)**: Hızlar, tırmanma oranları, menzil ve dayanım.
5.  **İtki Performansı (`propulsion`)**: Statik itki, güç tüketimi ve verimlilik.

## Analiz Koşulları

Her rapor, sonuçların hangi şartlar altında geçerli olduğunu belirten bir bağlam içermelidir:

| Parametre | Birim | Zorunlu | Açıklama |
| :--- | :--- | :--- | :--- |
| **total_mass** | `g` | Evet | Analiz anındaki toplam uçuş ağırlığı. |
| **cg_position_x** | `mm` | Evet | Analiz anındaki Ağırlık Merkezi (CG) konumu. |
| **altitude_msl** | `m` | Hayır | Analiz irtifası (Varsayılan: 0). |
| **temperature** | `C` | Hayır | Ortam sıcaklığı (Varsayılan: 15). |
| **air_density** | `kg/m³` | Hayır | Hava yoğunluğu (Varsayılan: 1.225). |

## Yorumlama ve Bayraklar

Setuav rapor formatı, "Stable", "Unstable", "Feasible" gibi metinsel yargılar veya bayraklar (flags) **içermez**. Rapor formatı, sadece objektif, hesaplanmış mühendislik verilerini saklar. Bu verilerin yorumlanması (örneğin %5 statik marjın "yeterli" olup olmadığı), veriyi okuyan mühendisin veya aracın sorumluluğundadır.

## Şema Referansı

Rapor dosyaları `schemas/report.json` şeması kullanılarak doğrulanabilir.

```bash
python3 validate.py my_analysis_result.yaml schemas/report.json
```
