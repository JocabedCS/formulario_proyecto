from django import forms


class RegistroForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        required=True,
        error_messages={
            "required": "El nombre es obligatorio.",
            "max_length": "Máximo 50 caracteres."
        },
        widget=forms.TextInput(attrs={
            "placeholder": "Escribe tu nombre"
        })
    )

    edad = forms.IntegerField(
        min_value=1,
        max_value=120,
        error_messages={
            "required": "La edad es obligatoria.",
            "min_value": "Debe ser mayor a 0.",
            "max_value": "Edad no válida."
        },
        widget=forms.NumberInput(attrs={"placeholder": "Edad"})
    )

    correo = forms.EmailField(
        required=True,
        error_messages={
            "required": "El correo es obligatorio.",
            "invalid": "Correo electrónico no válido."
        },
        widget=forms.EmailInput(attrs={"placeholder": "ejemplo@correo.com"})
    )

    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    genero = forms.ChoiceField(
        choices=[
            ("", "Seleccione un género"),
            ("M", "Masculino"),
            ("F", "Femenino"),
            ("O", "Otro")
        ],
        error_messages={
            "required": "Seleccione un género."
        }
    )

    archivo = forms.FileField(
        required=False
    )

    comentarios = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Escribe tus comentarios...",
            "rows": 4
        })
    )

    # ------------------------------------
    # ✅ NUEVO CAMPO AGREGADO: TELEFONO
    # ------------------------------------
    telefono = forms.CharField(
        required=False,
        max_length=10,
        min_length=10,
        error_messages={
            "max_length": "El teléfono debe tener 10 dígitos.",
            "min_length": "El teléfono debe tener 10 dígitos."
        },
        widget=forms.TextInput(attrs={
            "placeholder": "Teléfono (10 dígitos)"
        })
    )


    # -------------------------
    # VALIDACIONES PERSONALIZADAS
    # -------------------------

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    def clean_comentarios(self):
        comentarios = self.cleaned_data.get("comentarios")
        if comentarios in [None, "None"]:
            return ""
        if len(comentarios) > 300:
            raise forms.ValidationError("Máximo 300 caracteres.")
        return comentarios

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")

        if telefono:
            if not telefono.isdigit():
                raise f
