import os
import zipfile

# Create directory structure for Coffee Shop project
os.makedirs('coffee_shop/frontend', exist_ok=True)
os.makedirs('coffee_shop/backend', exist_ok=True)

# Frontend: Create a basic React.js app (mock files)
frontend_app_js = """
import React from 'react';

function App() {
  return (
    <div>
      <h1>Welcome to the Coffee Shop</h1>
    </div>
  );
}

export default App;
"""

frontend_package_json = """
{
  "name": "coffee-shop-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
"""

# Backend: Create a basic NestJS app (mock files)
backend_app_ts = """
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
"""

backend_service_ts = """
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Welcome to the Coffee Shop Backend!';
  }
}
"""

backend_main_ts = """
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
"""

backend_package_json = """
{
  "name": "coffee-shop-backend",
  "version": "1.0.0",
  "main": "dist/main.js",
  "scripts": {
    "start": "nest start",
    "build": "nest build"
  },
  "dependencies": {
    "@nestjs/common": "^9.0.0",
    "@nestjs/core": "^9.0.0"
  }
}
"""

# Create the files in the respective directories
with open('coffee_shop/frontend/App.js', 'w') as f:
    f.write(frontend_app_js)

with open('coffee_shop/frontend/package.json', 'w') as f:
    f.write(frontend_package_json)

with open('coffee_shop/backend/app.controller.ts', 'w') as f:
    f.write(backend_app_ts)

with open('coffee_shop/backend/app.service.ts', 'w') as f:
    f.write(backend_service_ts)

with open('coffee_shop/backend/main.ts', 'w') as f:
    f.write(backend_main_ts)

with open('coffee_shop/backend/package.json', 'w') as f:
    f.write(backend_package_json)

# Zip the directory
zip_filename = 'coffee_shop_project.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk('coffee_shop'):
        for file in files:
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), os.path.join('coffee_shop', '..')))

zip_filename
