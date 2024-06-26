# -*- coding: utf-8 -*-
"""Modelos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11bUbvYyL9p3chivJMFwt_VS2F7ED_JJT
"""

import pandas as pd
pip install pandas scikit-learn streamlit







df = pd.read_csv('/kaggle/input/fraude/PS_20174392719_1491204439457_log.csv')

df.head(10)

df.shape

df.info()

df.describe()

any_nulls = df.isna().any().any()
print(f"¿Hay algún valor nulo en el DataFrame? {any_nulls}")

# Verificar si hay algún valor nulo en cada columna
any_nulls_per_column = df.isna().any()
print(any_nulls_per_column)

# Codificar variables categóricas
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

# Escalar características numéricas
scaler = StandardScaler()
df[['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']] = scaler.fit_transform(
    df[['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]
)

df.info()

# Definir las características y la variable objetivo
X = df.drop(['isFraud', 'nameOrig', 'nameDest', 'isFlaggedFraud'], axis=1)
y = df['isFraud']

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
clf = DecisionTreeClassifier(random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = clf.predict(X_test)

# Mostrar el reporte de clasificación
print(classification_report(y_test, y_pred))

# Mostrar la matriz de confusión
print(confusion_matrix(y_test, y_pred))

"""**Gradient Boosting**"""

# Crear el modelo
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Entrenar el modelo
gb_model.fit(X_train, y_train)

# Hacer predicciones
y_pred = gb_model.predict(X_test)

# Evaluar el modelo
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""**Support Vector Machines (SVM)**"""

# Crear el modelo
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')

# Entrenar el modelo
svm_model.fit(X_train, y_train)

# Hacer predicciones
y_pred = svm_model.predict(X_test)

# Evaluar el modelo
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
