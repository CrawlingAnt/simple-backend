from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `class` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL  COMMENT '班级名'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `students` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL  COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL  COMMENT '密码',
    `no` VARCHAR(10) NOT NULL  COMMENT '学号',
    `Class_id` INT NOT NULL,
    CONSTRAINT `fk_students_class_36c748b8` FOREIGN KEY (`Class_id`) REFERENCES `class` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL  COMMENT '教师名',
    `pwd` VARCHAR(32) NOT NULL  COMMENT '密码',
    `tno` VARCHAR(10) NOT NULL  COMMENT '教师号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10) NOT NULL  COMMENT '课程名',
    `teacher_id` INT NOT NULL,
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `students_course` (
    `students_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`students_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_students_co_student_cea02e` (`students_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
