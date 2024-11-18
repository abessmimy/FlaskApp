from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    result = ""
    if request.method == 'POST':
        try:
            grades = [float(request.form[f'grade{i}']) for i in range(1, 4)]
            attendance = float(request.form['attendance'])
            avg = sum(grades) / 3
            status = "Aprobado" if avg >= 40 and attendance >= 75 else "Reprobado"
            result = f"Promedio: {avg:.2f}, Estado: {status}"
        except ValueError:
            result = "Error en los datos ingresados"
    return render_template('exercise1.html', result=result)

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    result = ""
    if request.method == 'POST':
        names = [request.form[f'name{i}'] for i in range(1, 4)]
        largest_name = max(names, key=len)
        result = f"Nombre más largo: {largest_name}, Longitud: {len(largest_name)}"
    return render_template('exercise2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
