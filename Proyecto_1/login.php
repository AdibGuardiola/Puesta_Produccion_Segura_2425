<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario usando los nombres correctos
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);

    // Leer el archivo de usuarios registrados
    $file = fopen("usuarios_registrados.txt", "r");

    if ($file) {
        $user_found = false;
        
        // Leer cada línea del archivo de usuarios
        while (($line = fgets($file)) !== false) {
            // Dividir la línea en email y contraseña usando la coma como separador
            list($registered_email, $registered_password) = explode(",", trim($line));

            // Verificar si el email y contraseña ingresados coinciden con los registrados
            if ($email === trim($registered_email) && $password === trim($registered_password)) {
                $user_found = true;
                break;
            }
        }

        fclose($file);

        if ($user_found) {
            echo "Bienvenido, has iniciado sesión correctamente.";
        } else {
            echo "Correo electrónico o contraseña incorrectos.";
        }
    } else {
        echo "Error al abrir el archivo.";
    }
}
?>
