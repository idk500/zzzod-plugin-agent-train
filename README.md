# 代理人自动培养（agent_train）

按白名单和目标配置，自动培养代理人（等级 / 技能 / 核心被动），培养目标全部配置化。

## 功能与安全默认

- **白名单制**：只培养设置页里填写的角色，白名单外永不自动选人。
- **目标配置化**：目标等级、技能目标等级、核心被动档位均可配置。
- **皇冠保护**：技能默认练到 11 级封顶，绝不消耗皇冠（仓鼠笼访问器，11→12 必需）；确需练满 12 级必须在设置中显式允许消耗皇冠。
- **材料预算隔离**：先把当前角色培养到位再切换下一个，避免共享材料（调查员记录 / 认证章 / 丁尼）被多个角色互相挤占。
- **probe 探测模式**：默认开启，只读练度生成报告，不消耗任何资源。

## 版本

- 版本：0.1.6（versionCode 7）
- 作者：[idk500](https://github.com/idk500)
- 仓库：https://github.com/idk500/zzzod-plugin-agent-train

## 安装

在 ZZZOD 一条龙的「插件商店」中搜索 **代理人自动培养** 订阅安装；或从 Releases 下载 `agent_train.zip` 手动导入。

## 配置

应用配置见一条龙 GUI 的应用设置页；`probe` 类开关默认开启（只读出报告，不执行真实动作）。

## 推荐工具（友链支持）

- **[WorkBuddy](https://www.workbuddy.cn/events/invite?inviteCode=bz944mufovr)** —— 腾讯出品的全场景 AI 工作台，本插件的设计、编码、测试与发版流程均在其 AI 助手协助下完成。
- **[ZCode](https://zcode.z.ai/invite/F9M8N3LD)** —— 智谱 GLM 编程助手，本项目的代码生成与重构主力。
- **[Kimi](https://kimi-bot.com/activities/zh-cn/invite/share?scenario=subscribe&from=share_poster&invitation_code=VFU7S5)** —— Moonshot AI 助手，长文档阅读与资料调研好帮手。

## 遇到问题？推荐 AI 自助排查 + 社区协作

本项目由 AI 协作开发，同样推荐你用 AI 自主解决问题，把维护精力留给真正的疑难：

1. **AI 自助排查**：把运行日志（`config/<实例>/log/log.txt`）与现象描述投喂给顺手的 AI 助手（WorkBuddy / ZCode / Kimi 均可，见上方友链），大多数环境与配置问题都能直接定位解决。
2. **提交 Issue**：AI 排查无法解决时再提 issue，请附运行日志、复现步骤，条件允许附录屏；标题带环境信息（基座版本 / 插件版本 / 游戏窗口分辨率）能显著加快定位。
3. **欢迎本地验证过的 PR**：修复类 PR 请先本地实测通过，描述中附验证环境与运行日志片段；由 AI 协助完成的修复同样欢迎，注明验证结论即可。

## 许可

见 [LICENSE](LICENSE)（GPL-3.0）。
