# DDD Architechture
Cấu trúc dự án Java Spring kết hợp best practices và kiến trúc hiện đại, phù hợp cho các dự án enterprise:

```
project-name/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── yourcompany/
│   │   │           └── projectname/
│   │   │               ├── application/          # Layer ứng dụng (use cases)
│   │   │               ├── domain/               # Core business logic
│   │   │               │   ├── model/            # Domain entities
│   │   │               │   ├── repository/       # Interface repository
│   │   │               │   └── service/          # Domain services
│   │   │               ├── infrastructure/       # Technical implementation
│   │   │               │   ├── config/           # Configuration classes
│   │   │               │   ├── persistence/      # JPA/Hibernate implementation
│   │   │               │   ├── web/              # Controllers, DTOs, Mappers
│   │   │               │   └── security/         # Security configuration
│   │   │               ├── interfaces/           # External interfaces (REST API, messaging)
│   │   │               └── ProjectNameApplication.java
│   │   └── resources/
│   │       ├── db/
│   │       │   └── migration/       # Flyway/Liquibase scripts
│   │       ├── i18n/                # Internationalization
│   │       ├── static/              # Static resources
│   │       ├── templates/           # Template files
│   │       ├── application.yml      # Main config
│   │       ├── application-dev.yml  # Environment-specific
│   │       └── logback-spring.xml   # Logging config
│   └── test/
│       └── java/
│           └── com/
│               └── yourcompany/
│                   └── projectname/
│                       ├── application/
│                       ├── domain/
│                       └── infrastructure/
├── .mvn/
├── .github/                       # CI/CD workflows
├── docker/                        # Docker configurations
├── docs/                          # API documentation
├── .gitignore
├── pom.xml                        # Maven config
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## Layer Architecture (Hexagonal/Onion)
+ Domain Layer: Chứa core business logic, entities và domain rules
+ Application Layer: Chứa use cases và workflow điều phối
+ Infrastructure Layer: Triển khai các technical details (DB, External services)
+ Interfaces Layer: Xử lý giao tiếp với bên ngoài (API, UI, Messaging)
## Cấu trúc package theo Domain-Driven Design (DDD)
```
domain/
├── order/
│   ├── model/
│   ├── repository/
│   └── service/
└── product/
    ├── model/
    ├── repository/
    └── service/
```
## Security Configuration
+ JWT Authentication
+ OAuth2 Integration
+ Role-based Authorization
+ Security Audit logging
## Persistence Layer
+ Separate Entity và DTO
+ JPA/Hibernate implementation
+ QueryDSL/JOOQ cho complex queries
+ Multiple DataSource support
## API Design
+ Versioning (v1, v2 trong URL)
+ Swagger/OpenAPI documentation
+ HATEOAS support
+ Global Exception Handler (@ControllerAdvice)
+ Request/Response validation
## Testing Infrastructure
+ Unit tests (JUnit 5 + Mockito)
+ Integration tests (@SpringBootTest)
+ Testcontainers cho database testing
+ API tests với RestAssured
## Monitoring & Observability
+ Spring Boot Actuator
+ Prometheus metrics
+ Distributed tracing (Sleuth/Zipkin)
+ Health checks
## CI/CD Pipeline
+ Multi-stage Docker build
+ SonarQube integration
+ Vulnerability scanning
+ Blue-Green deployment
## Advanced Configurations
+ Profile-based configuration
+ Database migration (Flyway)
+ Async configuration (@EnableAsync)
+ Scheduling (@EnableScheduling)
+ Circuit Breaker (Resilience4j)
## Common Utilities
+ Custom annotations
+ Global response wrapper
+ Pagination helper
+ Audit logging (Entity lifecycle tracking)
+ Cache abstraction layer

```xml
<!-- Core -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- Security -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<!-- Persistence -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- Documentation -->
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.2.0</version>
</dependency>

<!-- Monitoring -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<!-- Testing -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

## Functional Support
+ Tạo cấu trúc thư mục chuẩn theo DDD
+ Generate `pom.xml` với dependencies cơ bản
+ Tạo Dockerfile mẫu
+ Setup application class
+ Tạo các file config cơ bản (application.yml, logback,...)
+ Hỗ trợ tạo workflow thư mục cho CI/CD
## Usage
+ Cài đặt Python 3.6+: [Install Python](../PythonScript/README.md)
+ Chạy lệnh:
    ```bash
    python3 SpringBootScaffold.py \
            --group-id com.example \
            --artifact-id demo \
            --output-dir ~/projects
    ```






