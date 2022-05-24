import numpy as npimport pandas as pdfrom sklearn.preprocessing import LabelEncoderveri = pd.read_csv("telefon.csv")#sınıf sayısılabel_encoder = LabelEncoder().fit(veri.price_range)labels = label_encoder.transform(veri.price_range)classes = list(label_encoder.classes_)#girdi ve çıktılarx = veri.drop(["price_range"], axis=1)y = labels#verileri standartlaştırmafrom sklearn.preprocessing import StandardScalersc = StandardScaler()x = sc.fit_transform(x)#eğitim ve test verileni hazırlamafrom sklearn.model_selection import train_test_splitx_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)#çıktı değerlerinin kategorize edilmesifrom tensorflow.keras.utils import to_categoricaly_train = to_categorical(y_train)y_test = to_categorical(y_test)#Model Oluşturmafrom tensorflow.keras.models import Sequentialfrom tensorflow.keras.layers import Densemodel = Sequential()model.add(Dense(16, input_dim=20, activation="relu"))model.add(Dense(8, activation="relu"))model.add(Dense(4, activation="softmax"))model.summary()#modeli derlememodel.compile(learning_rate=0.3, loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])#modelin eğitilmesimodel.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=150)#Başarı değerleriprint("Ortalama eğitim kaybı: ", np.mean(model.history.history["loss"]))print("Ortalama eğitim başarısı: ", np.mean(model.history.history["accuracy"]))print("Ortalama doğrulama kaybı: ", np.mean(model.history.history["val_loss"]))print("Ortalama doğrulama başarımı: ", np.mean(model.history.history["val_accuracy"]))#Eğitim ve değerlendirme sonuçlarını grafikleştirmeimport matplotlib.pyplot as pltplt.plot(model.history.history["accuracy"])plt.plot(model.history.history["val_accuracy"])plt.title("Model Başarımları")plt.ylabel("Başarım")plt.xlabel("Epok sayısı")plt.legend(["Eğitim", "Test"], loc="upper left")plt.show()plt.plot(model.history.history["loss"])plt.plot(model.history.history["val_loss"])plt.title("Model Kayıpları")plt.ylabel("Kayıp")plt.xlabel("Epok sayısı")plt.legend(["Eğitim", "Test"], loc="upper left")plt.show()