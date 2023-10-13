import asyncio
import re
import os
from playwright.sync_api import Playwright, sync_playwright, expect

async def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=100, channel="msedge")

    PFthreshold = 1.25
    NPthreshold = 30000
    maxDrawdownThreshold = 10
    SRthreshold = 0.1

    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    # Change the collection name and paths accordingly
    collection = 'Strategy Collection FXView-Live EURMXN H1 162.json'
    Path = 'C:/megaEABot/Collections'
    downloadFolderPath = 'C:/megaEABot'
    initCollectionDownloadPath = os.path.join(Path, collection)

    page.goto('https://expert-advisor-studio.com/')
    page.get_by_label('Theme').select_option('dark')
    page.wait_for_timeout(3000)

    async def get_file_names():
        input_string = collection
        regex = r'([A-Z]+\d+)'
        matches = re.findall(regex, input_string)

        if matches and len(matches) >= 2:
            name1 = matches[0]
            name2 = matches[1]
            print(name1)
            print(name2)
        else:
            print("No matches found.")

    async def initial_setup():
        page.get_by_role("link", name="Tools").click()
        page.get_by_label("Collection capacity").select_option("300")
        page.get_by_role("link", name="Acceptance Criteria").click()
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").click()
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").press("Control+a")
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").fill("250")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").fill("50")
        page.locator("#validation-metrics-base").get_by_role("button", name="+ Add acceptance criteria").click()
        page.get_by_role("link", name="Minimum Sharpe ratio").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").fill("0.1")
        page.get_by_role("link", name="Available Indicators").click()
        page.locator("#toggle-entries").click()
        page.locator("#toggle-entries").click()
        page.locator("#toggle-exits").click()
        page.locator("#toggle-exits").click()
        page.get_by_role("row", name="Do not Exit").get_by_role("checkbox").uncheck()
        page.get_by_role("row", name="Exit Time").get_by_role("checkbox").uncheck()
        page.get_by_role("link", name="Data").click()
        page.get_by_role("link", name="Data Horizon").click()
        page.get_by_label("Maximum data bars").click()
        page.get_by_label("Maximum data bars").press("Control+a")
        page.get_by_label("Maximum data bars").fill("200000")
        page.get_by_label("Start date", exact=True).press("Control+a")
        page.get_by_label("Start date", exact=True).fill("2018-08-27")
        page.get_by_label("Use start date limit").check()
        page.get_by_role("link", name="Strategy ID -").click()
        page.get_by_role("link", name="Monte Carlo").click()
        page.get_by_label("Randomize history data").uncheck()
        page.get_by_label("Randomize spread").uncheck()
        page.get_by_label("Randomize slippage").uncheck()
        page.get_by_label("Randomly skip position entry").uncheck()
        page.get_by_label("Randomly skip position exit").uncheck()
        page.get_by_label("Randomize indicator parameters").check()
        page.get_by_label("Randomize backtest starting bar").check()
        page.get_by_role("link", name="Validation").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").fill("50")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").fill("50")
        page.get_by_role("button", name="+ Add validation criteria").click()
        page.get_by_role("link", name="Minimum profit factor").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").fill("1.01")
        page.get_by_role("link", name="Open the Generator, the Reactor, or the Validator").click()
        page.get_by_role("link", name="Reactor", exact=True).click()
        page.get_by_label("Data source").select_option("FXView-Demo")
        page.get_by_label("Symbol").select_option("USDCAD")
        page.get_by_label("Period").select_option("M1")
        page.locator("div").filter(has_text=re.compile(r"^2\. Strategy properties$")).click()
        page.get_by_label("Entry lots").click()
        page.get_by_label("Entry lots").press("Control+a")
        page.get_by_label("Entry lots").fill("0.01")
        page.get_by_label("Opposite entry signal").select_option("2")
        page.get_by_label("Stop Loss", exact=True).select_option("0")
        page.get_by_label("Type").select_option("3")
        page.get_by_role("spinbutton", name="Min (pips)").click()
        page.get_by_role("spinbutton", name="Min (pips)").press("Control+a")
        page.get_by_role("spinbutton", name="Min (pips)").fill("1")
        page.get_by_role("spinbutton", name="Max (pips)").click()
        page.get_by_role("spinbutton", name="Max (pips)").press("Control+a")
        page.get_by_role("spinbutton", name="Max (pips)").fill("1000")
        page.locator("div").filter(has_text=re.compile(r"^3\. Generator settings$")).click()
        page.locator("#search-best").select_option("4")
        page.get_by_label("Max entry indicators").select_option("8")
        page.get_by_label("Max exit indicators").select_option("4")
        page.get_by_label("Generate strategies with\nPreset Indicators").uncheck()
        page.get_by_label("Working minutes").click()
        page.get_by_label("Working minutes").press("Control+a")
        page.get_by_label("Working minutes").fill("720")
        page.get_by_role("link", name="Open the Generator, the Reactor, or the Validator").click()
        page.get_by_label("", exact=True).get_by_role("link", name="Reactor").click()
        page.locator("div").filter(has_text=re.compile(r"^1\. Historical data$")).click()
        page.get_by_role("button", name="Start").click()
        page.get_by_role("button", name="Stop").click()

    async def download_files():
        await page.wait_for_timeout(3000)
        await page.wait_for_selector('#eas-navbar-portfolio-link')
        await page.click('#eas-navbar-portfolio-link')
        await page.wait_for_selector('#portfolio-toolbar-export')
        await page.click('#portfolio-toolbar-export')
        await page.wait_for_selector('#export-portfolio-expert-mt5')

        download = await page.wait_for_event('download')
        await download.save_as(os.path.join(downloadFolderPath, download.suggested_filename()))

        await page.wait_for_selector('#eas-navbar-collection-link')
        await page.click('#eas-navbar-collection-link')
        collection_download = await page.wait_for_event('download')
        await collection_download.save_as(os.path.join(downloadFolderPath, collection_download.suggested_filename()))

        print('Portfolio saved to:', os.path.join(downloadFolderPath, download.suggested_filename()))
        print('Collected strategies saved to:', os.path.join(downloadFolderPath, collection_download.suggested_filename()))

    async def upload_collection(download_path):
        await page.wait_for_selector('#eas-navbar-collection-link')
        await page.click('#eas-navbar-collection-link')
        await page.locator("input[type='file']").set_input_files(download_path)
        print('Files uploaded')

    async def clear_portfolio():
        await page.wait_for_selector('#eas-navbar-portfolio-link')
        await page.click('#eas-navbar-portfolio-link')
        await page.wait_for_selector('#remove-all-button')
        await page.click('#remove-all-button')
        print('Portfolio deleted')

    async def add_all_collections():
        await page.wait_for_selector('#eas-navbar-collection-link')
        await page.click('#eas-navbar-collection-link')
        await page.get_by_role('button', name='+ Portfolio').click()
        await page.get_by_role('link', name='Add all').click()

        await page.wait_for_selector('#eas-navbar-portfolio-link')
        await page.click('#eas-navbar-portfolio-link')
        await page.wait_for_selector('#button-calculate')
        await page.click('#button-calculate')
        await page.wait_for_timeout(50000)
        print('Collections added to portfolio')

    async def get_collection_number():
        produced_strategies = await page.locator('#eas-collection-notification').text()
        print("No. of strategies produced:", produced_strategies)

    await initial_setup()
    # await upload_collection(initCollectionDownloadPath)
    # await add_all_collections()
    
    # Get the number of produced strategies
    produced_strategies = await page.locator('#eas-collection-notification').text()

    if int(produced_strategies) <= 40:
        print("No. of strategies produced:", produced_strategies)
        # Call strategyOne() if needed
    elif int(produced_strategies) <= 50:
        print("No. of strategies produced:", produced_strategies)
    elif int(produced_strategies) <= 200:
        print("No. of strategies produced:", produced_strategies)
        await strategyThree(page)
    elif int(produced_strategies) > 200:
        print("No. of strategies produced:", produced_strategies)
        await strategyFour(page)

    print(await analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold))
    print(await get_collection_number())
    print(await analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold))

async def analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold):
    await page.wait_for_selector('#eas-navbar-portfolio-link')
    await page.click('#eas-navbar-portfolio-link')

    await page.wait_for_selector('#backtest-output-table')

    def evaluate_threshold(value, threshold):
        return value > threshold

    async def get_value_and_threshold(selector, threshold):
        value_text = await page.locator(selector).text()
        value = float(value_text.split(' ')[0].replace(',', ''))
        return {'value': value, 'meetsThreshold': evaluate_threshold(value, threshold)}

    net_profit = await get_value_and_threshold('#backtest-profit', NPthreshold)
    max_drawdown = await get_value_and_threshold('#backtest-drawdown-percent', maxDrawdownThreshold)
    sharp_ratio = await get_value_and_threshold('#backtest-sharpe-ratio', SRthreshold)
    profit_factor = await get_value_and_threshold('#backtest-profit-factor', PFthreshold)

    print(f'Net Profit: {net_profit["value"]} | Max Drawdown: {max_drawdown["value"]}% | Sharp Ratio: {sharp_ratio["value"]} | Profit Factor: {profit_factor["value"]}')

    return {
        'netProfit': net_profit['value'],
        'maxDrawdown': max_drawdown['value'],
        'sharpRatio': sharp_ratio['value'],
        'profitFactor': profit_factor['value'],
        'isProfitFactorGreater': profit_factor['meetsThreshold'],
        'isNetProfitGreater': net_profit['meetsThreshold'],
        'isMaxDrawdownLess': not max_drawdown['meetsThreshold'],
        'isSharpRatioGreater': sharp_ratio['meetsThreshold']
    }

async def strategy_three(page):
    # Implement your strategy logic here
    pass

async def strategy_four(page):
    # Implement your strategy logic here
    pass

with sync_playwright() as p:
    asyncio.run(run(p))
