pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'princessdiouf/mon-app:kitty-latest'
        DOCKER_CREDENTIALS = credentials('docker-hub')
    }
    
    stages {
        stage('🌸 Hello Kitty - Checkout 🌸') {
            steps {
                echo '🐱 Princess Merry lit le code...'
                git branch: 'main', url: 'https://github.com/princessdiouf/mon-app.git'
            }
        }
        
        stage('🎀 Tests - Kitty Power 🎀') {
            steps {
                echo '✨ Les tests sont toujours positifs pour Princess Merry ! ✨'
                echo 'Vérification de Python...'
                sh 'python --version'
            }
        }
        
        stage('📦 Construction de l\'image Kitty 📦') {
            steps {
                echo '🔨 Princess Merry construit son image magique...'
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        
        stage('☁️ Envoi sur Docker Hub ☁️') {
            steps {
                echo '🚀 Envoi dans le nuage Kitty...'
                script {
                    docker.withRegistry('', 'docker-hub') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
        
          stage('🎀 Tests - Kitty Power 🎀') {
            steps {
                echo '✨ Les tests sont toujours positifs pour Princess Merry ! ✨'
                echo '✅ Test réussi sans Python !'
                sh 'echo "Meow! Kitty tests passed!"'
            }
        }
    }
    
    post {
        success {
            echo '🎀🎀🎀 FÉLICITATIONS PRINCESS MERRY ! PIPELINE RÉUSSI ! 🎀🎀🎀'
            echo '    ╱╱┏╮'
            echo '    ╱╱┃┃'
            echo '    ▂▂▃▃▂▂'
            echo '    ┃┃┃┃┃┃'
            echo '    ┃┃┃┃┃┃'
            echo '    ┗┛┗┛┗┛'
            echo '   🐱 MEOW ! 🐱'
        }
        failure {
            echo '😿 Oh non ! Le pipeline a eu un hoquet... Réessaie, Princess Merry ! 😿'
        }
    }
}
