# 🎯 Customer Segmentation & Actionable Insights with RFM & K-Means

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📖 Proje Özeti (Project Overview)
Bu proje, online bir perakende şirketinin işlem verilerini kullanarak **RFM (Recency, Frequency, Monetary)** analizi ve **K-Means Kümeleme** algoritması ile müşteri segmentasyonu yapmayı amaçlar.

Elde edilen segmentler, makine öğrenmesi (Unsupervised Learning) ve iş kuralları (Rule-Based) birleştirilerek eyleme dönüştürülebilir bir **Pazarlama Aksiyon Planı**na çevrilmiştir.

---

## 💼 İş Problemi (Business Problem)
Şirket, müşterilerini tek bir kitle olarak görmekte ve herkese aynı pazarlama stratejisini uygulamaktadır. Bu durum:
1.  Pazarlama bütçesinin verimsiz kullanılmasına,
2.  Yüksek potansiyelli (VIP) müşterilerin fark edilememesine,
3.  Kayıp (Churn) riski taşıyan müşterilerin geri kazanılamamasına yol açmaktadır.

**Hedef:** Müşterileri davranışlarına göre gruplara ayırıp, her gruba özel strateji geliştirmek.

---

## 🛠 Kullanılan Teknolojiler ve Yöntemler
* **Dil:** Python
* **Kütüphaneler:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Algoritmalar:**
    * RFM Analizi (Recency, Frequency, Monetary Metrics)
    * K-Means Clustering (Elbow Method ile optimum K belirlendi)
    * Rule-Based Segmentation (İşletme kurallarına göre son etiketleme)

---

## 📊 Veri Analizi Süreci (Analysis Pipeline)

### 1. Veri Hazırlığı (Data Preprocessing)
* **Veri Seti:** UCI Machine Learning Repository - Online Retail II.
* **Temizlik:** İade faturaları (`C` ile başlayanlar) ve eksik `Customer ID` değerleri veri setinden çıkarıldı.
* **Feature Engineering:** `TotalPrice` (Quantity * Price) hesaplandı.

### 2. RFM Metriklerinin Hesaplanması
Her müşteri için aşağıdaki metrikler oluşturuldu:
* **Recency (Yenilik):** Müşterinin son alışverişinden bugüne geçen gün sayısı.
* **Frequency (Sıklık):** Toplam eşsiz işlem sayısı.
* **Monetary (Parasal Değer):** Toplam harcama tutarı.

### 3. Ölçeklendirme ve Kümeleme (Scaling & Clustering)
* Veriler `MinMaxScaler` ile 0-1 arasına sıkıştırıldı.
* **Elbow Method (Dirsek Yöntemi)** kullanılarak optimum küme sayısı **K=3** (ve alternatif olarak K=4) analiz edildi.

### 4. Aksiyon Planı (Action Plan)
K-Means sonuçları ve işletme öncelikleri birleştirilerek müşteriler 3 ana kategoriye ayrıldı:

| Segment | Kriterler (Örnek) | Aksiyon Önerisi |
| :--- | :--- | :--- |
| **👑 VIP Müşteriler** | Son 53 gün içinde gelmiş, 10+ alışveriş, Yüksek Ciro | **Özel Hediye Gönder** 🎁 |
| **💤 Kaybedilenler** | 600+ gündür yok, çok az alışveriş yapmış | **Standart İndirim Maili** 📧 |
| **💳 Sadık/Potansiyel** | Ortalama değerlere sahip geniş kitle | **Sadakat Kartı Öner** 💳 |

---

## 📈 Proje Çıktıları (Visuals & Results)

### 1. Müşteri Segment Dağılımı
Hangi grupta kaç müşterimiz var? Pazarlama bütçesi buna göre ayarlanmalı.

![Proje Görseli](Images/Bar.png)

### 2. 3 Boyutlu Segmentasyon Görünümü
Müşterilerin 3 boyutlu uzayda (Recency - Frequency - Monetary) konumlanması. VIP müşterilerin (Sarı) diğerlerinden ne kadar ayrıştığına dikkat edin.

![3D Model](Images/3D%20Model.png)
├── RFM_Analysis.ipynb       # Tüm analizin yapıldığı Jupyter Notebook
├── requirements.txt         # Gerekli kütüphaneler
└── README.md                # Proje dokümantasyonu
