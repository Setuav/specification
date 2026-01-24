# Performans ve Analiz Raporları

Setuav Standardı, sadece İHA tasarımını değil, bu tasarımın analiz sonuçlarını saklamak ve paylaşmak için de bir yapı sunar. Bu bölüm, performans raporlarının nasıl yapılandırıldığını açıklar.

## Genel Bakış

Bir tasarım dosyasından (`design.yaml`) farklı olarak, performans raporları (`report.yaml`), bir analiz aracı veya test süreci tarafından üretilen **çıktıları** temsil eder. Bu ayrım, tasarım verileri ile sonuç verilerinin yaşam döngülerini birbirinden ayırır.

## Rapor Yapısı

Bir Setuav performans raporu (`report.json` şeması), dört ana kategoride toplanan **saf sayısal verilerden** oluşur:

1.  **Aerodinamik (`aerodynamics`)**: Temel aerodinamik katsayılar ve polarlar.
2.  **Stabilite (`stability`)**: Statik stabilite metrikleri ve türevler.
3.  **Uçuş Performansı (`flight`)**: Hızlar, tırmanma oranları, menzil ve dayanım.
4.  **İtki Performansı (`propulsion`)**: Statik itki, güç tüketimi ve verimlilik.

## Yorumlama ve Bayraklar

Setuav rapor formatı, "Stable", "Unstable", "Feasible" gibi metinsel yargılar veya bayraklar (flags) **içermez**. Rapor formatı, sadece objektif, hesaplanmış mühendislik verilerini saklar. Bu verilerin yorumlanması (örneğin %5 statik marjın "yeterli" olup olmadığı), veriyi okuyan mühendisin veya aracın sorumluluğundadır.

## Şema Referansı

Rapor dosyaları `schemas/report.json` şeması kullanılarak doğrulanabilir.

```bash
python3 validate.py my_analysis_result.yaml schemas/report.json
```
