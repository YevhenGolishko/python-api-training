node {

    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/YevhenGolishko/python-api-training.git'
    }
    stage("Install deps"){
        sh """
        # create new virtualenv
        rm -rf testvenv-${env.BUILD_ID}
        virtualenv -p python3 testvenv-${env.BUILD_ID}
        # activate virtualenv
        . testvenv-${env.BUILD_ID}/bin/activate
        pip install -r requirements.txt
        """
    }
    stage('Test'){
        sh 'pytest tests -sv --alluredir=allure_results'
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
