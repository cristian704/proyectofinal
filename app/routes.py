from flask import Blueprint, render_template, request, session, redirect, url_for
import random

main_bp = Blueprint("main", __name__)

CATEGORIES = {
    "colores": [
        ("red", "rojo"), ("blue", "azul"), ("green", "verde"),
        ("yellow", "amarillo"), ("black", "negro"),
        ("white", "blanco"), ("pink", "rosa"),
        ("orange", "naranja"), ("purple", "morado"),
        ("brown", "marrón")
    ],
    "numeros": [
        ("one", "uno"), ("two", "dos"), ("three", "tres"),
        ("four", "cuatro"), ("five", "cinco"),
        ("six", "seis"), ("seven", "siete"),
        ("eight", "ocho"), ("nine", "nueve"),
        ("ten", "diez")
    ],
    "animales": [
        ("dog", "perro"), ("cat", "gato"), ("lion", "león"),
        ("tiger", "tigre"), ("horse", "caballo"),
        ("cow", "vaca"), ("sheep", "oveja"),
        ("pig", "cerdo"), ("rabbit", "conejo"),
        ("bird", "pájaro")
    ],
    "frutas": [
        ("apple", "manzana"), ("banana", "plátano"),
        ("orange", "naranja"), ("grape", "uva"),
        ("strawberry", "fresa"), ("pineapple", "piña"),
        ("mango", "mango"), ("pear", "pera"),
        ("lemon", "limón"), ("watermelon", "sandía")
    ],
    "prendas": [
        ("shirt", "camisa"), ("pants", "pantalón"),
        ("shoes", "zapatos"), ("jacket", "chaqueta"),
        ("hat", "sombrero"), ("dress", "vestido"),
        ("socks", "calcetines"), ("gloves", "guantes"),
        ("belt", "cinturón"), ("coat", "abrigo")
    ],
    "paises": [
        ("spain", "españa"), ("france", "francia"),
        ("bolivia", "bolivia"), ("peru", "perú"),
        ("mexico", "méxico"), ("argentina", "argentina"),
        ("brazil", "brasil"), ("chile", "chile"),
        ("germany", "alemania"), ("italy", "italia")
    ],
    "comidas": [
    ("rice", "arroz"),
    ("bread", "pan"),
    ("meat", "carne"),
    ("fish", "pescado"),
    ("chicken", "pollo"),
    ("soup", "sopa"),
    ("salad", "ensalada"),
    ("egg", "huevo"),
    ("cheese", "queso"),
    ("pizza", "pizza")
],

"electrodomesticos": [
    ("television", "televisor"),
    ("radio", "radio"),
    ("refrigerator", "refrigerador"),
    ("washing machine", "lavadora"),
    ("microwave", "microondas"),
    ("blender", "licuadora"),
    ("fan", "ventilador"),
    ("vacuum cleaner", "aspiradora"),
    ("iron", "plancha"),
    ("air conditioner", "aire acondicionado")
],

"accesorios": [
    ("remote control", "control remoto"),
    ("speaker", "parlante"),
    ("headphones", "auriculares"),
    ("charger", "cargador"),
    ("battery", "batería"),
    ("usb cable", "cable usb"),
    ("antenna", "antena"),
    ("memory card", "tarjeta de memoria"),
    ("keyboard", "teclado"),
    ("mouse", "ratón")
],

"cuerpo": [
    ("head", "cabeza"),
    ("hair", "cabello"),
    ("eye", "ojo"),
    ("ear", "oreja"),
    ("nose", "nariz"),
    ("mouth", "boca"),
    ("hand", "mano"),
    ("arm", "brazo"),
    ("leg", "pierna"),
    ("foot", "pie")
]
}


@main_bp.route("/")
def index():
    return render_template(
        "index.html",
        categories=CATEGORIES.keys(),
        user={"username": "Invitado"}
    )


@main_bp.route("/play/<category>", methods=["GET", "POST"])
def play(category):

    if category not in CATEGORIES:
        return "Categoría no existe"

    if session.get("category") != category or "word" not in session:
        word, answer = random.choice(CATEGORIES[category])
        session["word"] = word
        session["answer"] = answer
        session["category"] = category
        session["result"] = ""

    if request.method == "POST":

        user_answer = request.form.get("answer", "").strip().lower()

        if user_answer == session["answer"]:
            session["result"] = "✔ Correcto"
        else:
            session["result"] = f"❌ Incorrecto, era: {session['answer']}"

        word, answer = random.choice(CATEGORIES[category])

        session["word"] = word
        session["answer"] = answer

        return redirect(url_for("main.play", category=category))

    return render_template(
        "play.html",
        category=category,
        word=session["word"],
        result=session["result"]
    )