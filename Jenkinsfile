node {

    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/YevhenGolishko/python-api-training.git'
    }
    stage("Install deps"){
        sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
    }
    stage('Test'){
        sh 'python3 -m pytest tests -sv --alluredir=allure_results'
    }
    stage('Report'){
        script {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure_results']]
            ])
        }
    }
}
