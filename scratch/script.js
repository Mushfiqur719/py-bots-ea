const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext({
    storageState: 'auth.json'
  });
  const page = await context.newPage();
  await page.goto('https://expert-advisor-studio.com/');
  await page.getByLabel('Theme').selectOption('dark');
  await page.getByRole('link', { name: 'Open the Generator, the Reactor, or the Validator' }).click();
  await page.getByRole('link', { name: 'Reactor', exact: true }).click();
  await page.getByLabel('Data source').selectOption('FXView-Demo');
  await page.getByLabel('Symbol').selectOption('EURSGD');
  await page.getByLabel('Period').selectOption('M1');
  await page.locator('div').filter({ hasText: /^2\. Strategy properties$/ }).click();
  await page.getByLabel('Entry lots').click();
  await page.getByLabel('Entry lots').press('Control+a');
  await page.getByLabel('Entry lots').fill('0.01');
  await page.getByLabel('Opposite entry signal').selectOption('2');
  await page.getByLabel('Stop Loss', { exact: true }).selectOption('0');

  // ---------------------
  await context.close();
  await browser.close();
})();