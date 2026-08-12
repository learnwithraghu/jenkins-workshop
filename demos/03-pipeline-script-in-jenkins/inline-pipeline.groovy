// Paste this into Jenkins under Pipeline → Definition → Pipeline script
// This file is a reference copy only — Jenkins does NOT read it from the repo.

pipeline {
    agent any

    stages {
        stage('Run') {
            steps {
                sh 'cd demos/03-pipeline-script-in-jenkins && python3 app.py'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed — check console output.'
        }
    }
}
