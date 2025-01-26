<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        canvas {
            border: 1px solid #000;
            background-color: #fff;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        
        const scale = 20;
        const rows = canvas.height / scale;
        const columns = canvas.width / scale;

        let snake;
        let apple;

        (function setup() {
            snake = new Snake();
            apple = new Apple();
            window.setInterval(update, 1000 / 15); // 15 frames per second
            window.addEventListener("keydown", e => snake.changeDirection(e));
        })();

        function update() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            snake.update();
            snake.draw();
            apple.draw();

            if (snake.eat(apple)) {
                apple.randomize();
            }

            if (snake.checkCollision()) {
                window.location.reload(); // Restart the game
            }
        }

        function Snake() {
            this.snakeArray = [{x: 5, y: 5}];
            this.direction = "RIGHT";
            
            this.update = function() {
                let head = {x: this.snakeArray[0].x, y: this.snakeArray[0].y};

                switch(this.direction) {
                    case "UP": head.y--; break;
                    case "DOWN": head.y++; break;
                    case "LEFT": head.x--; break;
                    case "RIGHT": head.x++; break;
                }

                this.snakeArray.unshift(head);
                this.snakeArray.pop();
            };

            this.changeDirection = function(event) {
                const keyPressed = event.keyCode;
                if (keyPressed === 37 && this.direction !== "RIGHT") this.direction = "LEFT";
                if (keyPressed === 38 && this.direction !== "DOWN") this.direction = "UP";
                if (keyPressed === 39 && this.direction !== "LEFT") this.direction = "RIGHT";
                if (keyPressed === 40 && this.direction !== "UP") this.direction = "DOWN";
            };

            this.eat = function(apple) {
                if (this.snakeArray[0].x === apple.x && this.snakeArray[0].y === apple.y) {
                    this.snakeArray.push({});
                    return true;
                }
                return false;
            };

            this.checkCollision = function() {
                let head = this.snakeArray[0];
                if (head.x < 0 || head.x >= columns || head.y < 0 || head.y >= rows) return true;
                for (let i = 1; i < this.snakeArray.length; i++) {
                    if (this.snakeArray[i].x === head.x && this.snakeArray[i].y === head.y) return true;
                }
                return false;
            };

            this.draw = function() {
                for (let i = 0; i < this.snakeArray.length; i++) {
                    ctx.fillStyle = (i === 0) ? "green" : "gray";
                    ctx.fillRect(this.snakeArray[i].x * scale, this.snakeArray[i].y * scale, scale, scale);
                }
            };
        }

        function Apple() {
            this.randomize = function() {
                this.x = Math.floor(Math.random() * columns);
                this.y = Math.floor(Math.random() * rows);
            };

            this.draw = function() {
                ctx.fillStyle = "red";
                ctx.fillRect(this.x * scale, this.y * scale, scale, scale);
            };

            this.randomize();
        }
    </script>
</body>
</html>
