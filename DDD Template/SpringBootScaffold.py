import os
import argparse
from pathlib import Path

TEMPLATES = {
    'pom.xml': """<?xml version="1.0" encoding="UTF-8"?>
                    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
                        <modelVersion>4.0.0</modelVersion>
                        <parent>
                            <groupId>org.springframework.boot</groupId>
                            <artifactId>spring-boot-starter-parent</artifactId>
                            <version>3.2.0</version>
                            <relativePath/>
                        </parent>

                        <groupId>{group_id}</groupId>
                        <artifactId>{artifact_id}</artifactId>
                        <version>1.0.0-SNAPSHOT</version>
                        <name>{project_name}</name>

                        <properties>
                            <java.version>17</java.version>
                            <springdoc.version>2.2.0</springdoc.version>
                        </properties>

                        <dependencies>
                            <dependency>
                                <groupId>org.springframework.boot</groupId>
                                <artifactId>spring-boot-starter-web</artifactId>
                            </dependency>
                            <dependency>
                                <groupId>org.springframework.boot</groupId>
                                <artifactId>spring-boot-starter-security</artifactId>
                            </dependency>
                            <dependency>
                                <groupId>org.springframework.boot</groupId>
                                <artifactId>spring-boot-starter-data-jpa</artifactId>
                            </dependency>
                            <dependency>
                                <groupId>org.springdoc</groupId>
                                <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
                                <version>${{springdoc.version}}</version>
                            </dependency>
                            <dependency>
                                <groupId>org.springframework.boot</groupId>
                                <artifactId>spring-boot-starter-actuator</artifactId>
                            </dependency>
                        </dependencies>

                        <build>
                            <plugins>
                                <plugin>
                                    <groupId>org.springframework.boot</groupId>
                                    <artifactId>spring-boot-maven-plugin</artifactId>
                                </plugin>
                            </plugins>
                        </build>
                    </project>
                    """,

    'Application.java':  """package {package_name};
                            import org.springframework.boot.SpringApplication;
                            import org.springframework.boot.autoconfigure.SpringBootApplication;

                            @SpringBootApplication
                            public class {application_class} {{
                                public static void main(String[] args) {{
                                    SpringApplication.run({application_class}.class, args);
                                }}
                            }}
                        """
}

def createProjectStructure(baseDir, groupId, artifactId):
    packagePath = os.path.join(*groupId.split('.')) + '/' + artifactId

    dirs = [
        f'src/main/java/{packagePath}/application',
        f'src/main/java/{packagePath}/domain',
        f'src/main/java/{packagePath}/infrastructure/config',
        f'src/main/java/{packagePath}/infrastructure/persistence',
        f'src/main/java/{packagePath}/infrastructure/web',
        f'src/main/java/{packagePath}/infrastructure/security',
        f'src/main/java/{packagePath}/interfaces',
        'src/main/resources/db/migration',
        'src/main/resources/i18n',
        'src/test/java/' + packagePath,
        'docker',
        'docs',
        '.github/workflows'
    ]

    for d in dirs:
        Path(os.path.join(baseDir, d)).mkdir(parents=True, exist_ok=True)

    with open(os.path.join(baseDir, 'pom.xml'), 'w') as f:
        f.write(TEMPLATES['pom.xml'].format(
            group_id=groupId,
            artifact_id=artifactId,
            project_name=baseDir
        ))

    appClass = f"{artifactId.capitalize()}Application"
    appPath = os.path.join(baseDir, f'src/main/java/{packagePath}/{appClass}.java')
    with open(appPath, 'w') as f:
        f.write(TEMPLATES['Application.java'].format(
            package_name=f"{groupId}.{artifactId}",
            application_class=appClass
        ))

    commonConfigs = [
        ('src/main/resources/application.yml', 'spring:\n  application:\n    name: ${project_name}\n'),
        ('src/main/resources/logback-spring.xml', '<!-- Logback config -->'),
        ('.dockerignore', 'target/\n*.jar\n'),
        ('Dockerfile', 'FROM eclipse-temurin:17-jdk-alpine\nVOLUME /tmp\nCOPY target/*.jar app.jar\nENTRYPOINT ["java","-jar","/app.jar"]')
    ]

    for filePath, content in commonConfigs:
        with open(os.path.join(baseDir, filePath), 'w') as f:
            f.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Spring Boot Project Structure')
    parser.add_argument('-g', '--group-id', required=True, help='Maven Group ID')
    parser.add_argument('-a', '--artifact-id', required=True, help='Maven Artifact ID')
    parser.add_argument('-o', '--output-dir', default='.', help='Output directory')
    
    args = parser.parse_args()
    print(args)
    project_dir = os.path.join(args.output_dir, args.artifact_id)
    createProjectStructure(project_dir, args.group_id, args.artifact_id)
    
    print(f"Project generated at: {project_dir}")
    print("Next steps:")
    print(f"cd {project_dir} && mvn clean install")