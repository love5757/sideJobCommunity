< sequelize sync command >

npm i sequelize mysql2
npm i -g sequelize-cli
sequelize init

npm install -g sequelize-auto
npm install -g mysql

sequelize-auto -o "./models" -d sidejob_proj -h localhost -u root -p 3306 -x password123 -e mysql
sequelize-auto -o "./api/sequelize/models" -d sidejob_proj -h soorokim.duckdns.org -u manager -p 19222 -x Javascript -e mysql

