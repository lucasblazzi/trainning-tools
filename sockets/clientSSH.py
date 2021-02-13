import paramiko

host = 'ip'
port = 22
user = 'username'
passwd = 'password'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, username=user, password=passwd)

while True:
    cmd = input('#')
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.readlines())
    print(stderr.readlines())

    
 st.markdown(
    """
<style>
body{
    margin: 0;
    padding: 0;
    min-height: 100vh;
    background: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: consolas;
}

.container{
    width: 1000px;
    position: relative;
    display: flex;
    justify-content: space-between;
}

.container .card{
    position: relative;
    cursor: pointer;
}

.container .card .face{
    width: 300px;
    height: 200px;
    transition: 0.5s;
}

.container .card .face.face1{
    position: relative;
    background: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1;
    transform: translateY(100px);
}

.container .card:hover .face.face1{
    background: #ff0057;
    transform: translateY(0);
}

.container .card .face.face1 .content{
    opacity: 0.2;
    transition: 0.5s;
}

.container .card:hover .face.face1 .content{
    opacity: 1;
}

.container .card .face.face1 .content img{
    max-width: 100px;
}

.container .card .face.face1 .content h3{
    margin: 10px 0 0;
    padding: 0;
    color: #fff;
    text-align: center;
    font-size: 1.5em;
}

.container .card .face.face2{
    position: relative;
    background: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
    transform: translateY(-100px);
}

.container .card:hover .face.face2{
    transform: translateY(0);
}

.container .card .face.face2 .content p{
    margin: 0;
    padding: 0;
}

.container .card .face.face2 .content a{
    margin: 15px 0 0;
    display:  inline-block;
    text-decoration: none;
    font-weight: 900;
    color: #333;
    padding: 5px;
    border: 1px solid #333;
}

.container .card .face.face2 .content a:hover{
    background: #333;
    color: #fff;
}
</style>
<body>
    <div class="container">
        <div class="card">
            <div class="face face1">
                <div class="content">
                    <img src="https://iconarchive.com/download/i100101/iynque/ios7-style/Stocks.ico">
                    <h3>Series</h3>
                </div>
            </div>
            <div class="face face2">
                <div class="content">
                    <p>This dashboard is used to monitor assets series from Jarvis Application (Keyspaces, Redis, S3)</p>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="face face1">
                <div class="content">
                    <h3>Products</h3>
                </div>
            </div>
            <div class="face face2">
                <div class="content">
                    <p>This dashboard is used to monitor products registration from Jarvis Application on Elasticsearch</p>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="face face1">
                <div class="content">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTZZ30XBxTqObda62aj3N-prDx4SbuLHhh_A&usqp=CAU">
                    <h3>Launch</h3>
                </div>
            </div>
            <div class="face face2">
                <div class="content">
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas cum cumque minus iste veritatis provident at.</p>
                        <a href="#">Read More</a>
                </div>
            </div>
        </div>
    </div>
</body>
""", unsafe_allow_html=True
)
