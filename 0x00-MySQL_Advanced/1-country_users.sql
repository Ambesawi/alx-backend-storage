-- Create the 'users' table if it doesn't exist
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);

-- Create a stored procedure to add the 'country' column if it doesn't exist
DELIMITER //
CREATE PROCEDURE AddCountryColumn()
BEGIN
    IF NOT EXISTS (SELECT * FROM information_schema.columns
                   WHERE table_name = 'users'
                   AND column_name = 'country') THEN
        ALTER TABLE `users`
        ADD COLUMN `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US';
    END IF;
END //
DELIMITER ;

-- Call the stored procedure to add the 'country' column conditionally
CALL AddCountryColumn;

