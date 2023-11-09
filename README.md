# selisihCpmsTmDocker

<ol> 
  <li>Windows 10 Pro 64-bit (10.0, Build 19041)</li>
  <li>Python 3.9.18 (main, Nov  1 2023, 14:35:47)</li
  <li>mysql ver: 5.5.68-MariaDB</li>
</ol>


# install app manual from github
<ol>
  <li>install mariadb from another pc, username with config { mysql_host: '192.168.0.42', mysql_user: 'hakim', mysql_password: 'sap123ok', mysql_db: 'trs' }</li>
  <li>$ git clone </li>
  
  
</ol>

# install app from dockerhub
<ol>
  <li>install mariadb from another pc, username with config { mysql_host: '192.168.0.42', mysql_user: 'hakim', mysql_password: 'sap123ok', mysql_db: 'trs' }</li>
  <li>$ docker pull hakimrevlim/selisih_cpms_tm:v1</li>
  <li>$ docker run -p 5000:5000 hakimrevlim/selisih_cpms_tm:v1</li>
  <li>open browser, type url [ 192.168.0.39:5000 ]</li>
</ol>
