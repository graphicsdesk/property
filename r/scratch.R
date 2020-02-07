library(tidyverse)

a <- read.csv('../columbia.csv')
b <- read.csv('../out-20.csv')

a %>% anti_join(b, by = 'latitude') %>% nrow()