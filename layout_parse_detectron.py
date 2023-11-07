// get response from genext - activates scraper
app.post('/genext', async (req, res) => {
	res.status(503).json({message: "Genext endpoint closed for maintenance"})	// closed as spawning too many chrome windows
	return;
	let response = "";
	console.log(req.body.prompt);
	let driver = await new Builder().forBrowser(Browser.CHROME).build();
	try {
		await driver.get('https://genext.bmwgroup.net/#/chat');
		await driver.sleep(2000)
		await driver.findElement(By.id('idToken2')).sendKeys('Q510579');
		await driver.findElement(By.id('idToken3')).sendKeys('Thisisanewpasswordpleaselogin:',Key.ENTER)
		await driver.sleep(500)
		await driver.findElement(By.xpath('/html/body/app-root/genext-sidebar/div/div[2]/div/div/app-landing/div/div[3]/div/ds-box/div/div[3]/ds-box-content/div[2]/a')).click();
		
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[1]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[2]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[3]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[4]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[5]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[6]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[7]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('//*[@id="disclaimer-en"]/div[2]/ds-form-field/div/ds-checkbox-group[8]/div')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('/html/body/div/div[2]/div/div/ds-box/div/div[4]/ds-box-footer/ds-button')).click();
		await driver.sleep(50);
		await driver.findElement(By.xpath('/html/body/app-root/genext-sidebar/div/div[2]/div/div/app-landing/div/div[3]/div/ds-box/div/div[3]/ds-box-content[2]/div[2]/button')).click();
		await driver.sleep(500);
		await driver.findElement(By.xpath('/html/body/app-root/genext-sidebar/div/div[2]/div/div/app-chat/div/ds-box/div/div[3]/ds-box-content/div[2]/div/div[2]/genext-chat-parameters/form/ds-form-field[3]/div/div/input')).sendKeys('0');
		let prompt = "here is my question: " + JSON.stringify(req.body.question) + " from this data (exclude data from LLP2-1): " + JSON.stringify(req.body.data) + " your response must start with X_X";
		await driver.findElement(By.xpath('/html/body/app-root/genext-sidebar/div/div[2]/div/div/app-chat/div/ds-box/div/div[3]/ds-box-content/div[2]/div/div[1]/div[2]/genext-chat-prompt/form/ds-form-field/div/div/textarea')).sendKeys(prompt);
		await driver.findElement(By.xpath('/html/body/app-root/genext-sidebar/div/div[2]/div/div/app-chat/div/ds-box/div/div[3]/ds-box-content/div[2]/div/div[1]/div[2]/div/div[2]/button')).click();
		await driver.sleep(10000)
		
		let html = await driver.getPageSource()

		let html1 = html.split("<p>X_X");
		let html2 = html1[1].split("</p>");
		let response = html2[0];
		await driver.quit();

		res.status(200).json({"response":response});

	} finally {
		

		
	}

});
