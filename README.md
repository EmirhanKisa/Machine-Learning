Bu depo, aynı makine öğrenimi problemi için geliştirilmiş ebebeyinli ve ebebeyinsiz iki farklı Python kodunu içerir.

Kodlar Hakkında
Ebebeyinli Kod:
Bu kodda, model eğitimi sırasında hedef değişkeni (sınav notu) tahmin etmek için önceki dönem notları gibi ebeveyn (parent) özellikleri kullanılmıştır. Bu yöntem, modelin geçmiş performans bilgilerini de dikkate alarak daha iyi sonuçlar verebilir.

Ebebeyinsiz Kod:
Bu versiyonda ise ebeveyn (parent) özellikleri kullanılmadan, yalnızca doğrudan gözlemlenen diğer özelliklerle model oluşturulmuştur. Daha sade ama bazen daha az bilgi içeren bir yaklaşımı temsil eder.

Kullanım
ebebeyinli.py: Ebeveyn özellikleri ile çalışan modelin kodu.

ebebeyinsiz.py: Ebeveyn özellikleri olmadan çalışan modelin kodu.

Sonuçlar
Ebebeyinli modelin daha az değişken içermesi, modelin sadeleştirilmesine rağmen doğruluk performansında herhangi bir düşüşe neden olmamış; tam tersine, daha yüksek bir başarı sağlamıştır. 
Bu durum, eğitim verisiyle çalışan modellerde değişken seçiminin ne kadar önemli olduğunu ortaya koymaktadır. 
Karmaşık ve çok değişkenli modeller her zaman daha doğru sonuçlar üretmeyebilir; bazen sadece anlamlı ve güçlü ilişkili birkaç değişkenle daha verimli ve başarılı sonuçlar elde edilebilir. 

Bu projedeki kodlar, aşağıdaki makaleden ve oradaki yöntemlerden esinlenerek geliştirilmiştir:

S. K. Singh, S. Goswami, S. Nagar, M. Kaur, N. Rakesh and M. K. Goyal, "Machine Learning Based Predicting Student’s Grade," 2022 International Conference on Fourth Industrial Revolution Based Technology and Practices (ICFIRTP), Uttarakhand, India, 2022, pp. 234-237, doi: 10.1109/ICFIRTP56122.2022.10059421.

Projeyi yaparken bu makaleyi referans aldım ve kendi verimle/amaçlarımla uyarladım.
