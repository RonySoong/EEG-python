#脑电情感标签
EEG_lable = []
with open(r"EEG_emotion_category.txt") as f:
    for line in f.readlines():
        EEG_lable.append(int(line.split()[0]))
#脑电特征
EEG_feature = []
i = 0
with open(r"EEG_feature.txt") as f:
    for line in f.readlines():
        tmp = []
        for num in line.split():
            tmp.append(float(num))
        EEG_feature.append(tmp)
#聚类分析
#题目一共给9类，所以将聚心设计为9个
#kMeans
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 9)
result = kmeans.fit(EEG_feature)
print(result)
print(result.labels_)
#Agglomerative Clustering
from sklearn.cluster import AgglomerativeClustering
agg = AgglomerativeClustering(n_clusters = 9)
result = agg.fit(EEG_feature)
print(result)
print(result.labels_)

