import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv("agriculture.csv")
print(data.isnull().sum())  # nan checking columns each other
print(data.shape)
print(data['Production'])

production_count = data["Production"].fillna(data["Production"].median())
print("production count -->\n{}".format(production_count))
data_pre = data.fillna(data["Production"].median())
data_pre.drop('State_Name', axis=1, inplace=True)
print(data_pre)

cy = data_pre["Crop_Year"].value_counts().sort_index()
data_pre.dropna(how="any", inplace=True)
print("duplicate entries", len(data_pre[data_pre.duplicated()]))
print()

data_pre["District_Name"] = data_pre["District_Name"].apply(lambda x: x.lower().capitalize())
a = data_pre.groupby("Crop_Year")['Area'].sum().sort_index(ascending=True).index
b = data_pre.groupby("Crop_Year")['Area'].sum().sort_index(ascending=True).values

frame = {"Crop_Year": a, "Area": b}
structure = pd.DataFrame(frame)

dn = data_pre.groupby("District_Name")['Area'].sum().sort_index(ascending=True)
dis = data_pre[data_pre.Crop_Year == 2013].groupby("District_Name")["Area"].sum().sort_index(ascending=False).index
area = data_pre[data_pre.Crop_Year == 2013].groupby("District_Name")["Area"].sum().sort_index(ascending=False).values
dn_frame = {"dn": dis, "area": area}
dn_structure = pd.DataFrame(dn_frame)
print(dn_structure)

# ----------------------------------------------------------------------------------------------------------------------#
fig = go.Figure(data=go.Scatter(x=structure["Crop_Year"], y=structure["Area"], marker_color=structure["Crop_Year"]))
fig.update_layout(title="India Agriculture", xaxis=dict(tickmode="linear", dtick=1))
fig.show()

fig = px.bar(dn_frame, x="dn", y="area", color="area", height=500, width=1100, text="area", title='Year vs. Area')
fig.show()

print(data_pre['Season'].value_counts())
print(data_pre['Crop'].value_counts())
cs = data_pre.groupby(["Season", "Crop"])["Production"].sum()
cs_frame = pd.DataFrame({"production": cs}).reset_index()
print(cs_frame)
print(cs_frame['Season'].value_counts())

weather_y = cs_frame[cs_frame["Season"] == 'Whole Year']
el = cs_frame[cs_frame["Season"] != 'Whole Year']
spending_group = pd.concat([weather_y.sample(frac=0.3), el])

fig = px.sunburst(spending_group, path=["Season", "Crop"], values="production")
fig.show()

fig = px.scatter(data_pre, x="Production", y="Area", size="Crop_Year", color='Season',
                 size_max=10, title="area vs production", log_x=True)
fig.show()

data_labeling = {"Rabi": 0, "Whole Year": 1, "Kharif": 2}
data_pre["Season_data"] = data_pre["Season"].apply(lambda x: data_labeling[x])
data1 = data_pre.drop("Season", axis='columns')


from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = data1[["Crop_Year", "Area", "Production"]].values
y = data1["Season_data"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5, shuffle=True)

# sc = StandardScaler()
# X_train_std = sc.fit_transform(X_train)
# X_test_std = sc.fit_transform(X_test)

# knn_reg = KNeighborsClassifier(n_neighbors=24, n_jobs=-1)
# knn_reg.fit(X_train_std, y_train)
#
# print(f"TAMILNADU KNN regression loss => {knn_reg.score(X_test_std, y_test)}")


val_acc = []
train_acc = []
for i in range(1, 31):
    knn = RandomForestClassifier(i, n_jobs=-1)
    knn.fit(X_train, y_train)
    val_acc.append(knn.score(X_test, y_test))
    train_acc.append(knn.score(X_train, y_train))
    print(f"TAMLINADO tree machine learning of distance -> {i} score -> {knn.score(X_test, y_test)}")

plt.plot(val_acc, "*--", label="test_acc")
plt.plot(train_acc, "^--", label="train_acc")
plt.xlabel("distance")
plt.ylabel("acc")
plt.legend()
plt.show()
