node {

    stage("Checkout repo"){
        git branch: 'main',
        url: 'https://github.com/YevhenGolishko/python-api-training.git'
    }
    stage("Install deps"){
        sh 'virtualenv venv && pip install -r requirements.txt'
    }

}
