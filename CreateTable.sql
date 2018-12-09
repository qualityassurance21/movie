DROP TABLE if EXISTS `bookInfo`;
CREATE TABLE `bookInfo` (
  `id` varchar(255) NOT NULL COMMENT '编号',
  `title` varchar(255) NOT NULL COMMENT '书名',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `averageRating` varchar(255) DEFAULT NULL COMMENT '评价得分',
  `ratingCount` varchar(255) DEFAULT NULL COMMENT '评价人数',
  `kinds` varchar(255) DEFAULT NULL COMMENT '标签',
  `abstract` varchar(8000) DEFAULT NULL COMMENT '摘要',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='图书';

DROP TABLE if EXISTS 	`movieInfo`;
CREATE TABLE `movieInfo` (
`id` VARCHAR(20) Not NULL COMMENT '编号' PRIMARY KEY,
`title` VARCHAR(255) NOT NULL COMMENT '电影名字',
`casts` VARCHAR(255) COMMENT '演员',
`directors` VARCHAR(255) COMMENT '导演',
`rate` VARCHAR(10) COMMENT '评分',
`star` VARCHAR(10) COMMENT '评论得分',
`style` VARCHAR(10) COMMENT '类型'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='电影简介';