import discord
import discord.ext.tasks
from random import randint as random_randint
# import datetime
from datetime import datetime
# import time
# import json
from json import dumps as json_dumps
from json import loads as json_loads
import io
import inspect
import re
import os
# import math




startTime = (datetime.now())

# timeOffset = (((datetime.utcnow()) - (datetime.now())).total_seconds())
timeOffset = (((datetime.utcfromtimestamp(startTime.timestamp())) - (datetime.fromtimestamp(startTime.timestamp()))).total_seconds())

activeHelpEmbeds = []

statusScheduleOverridden = False
statusSchedulePosition = -1



discordClassNamesDict = {}
discordClassAttributesDict = {}
discordClassNameAttributesDict = {}
indexJson = {}
virtualParameters = None
generatedEmbeds = {}
typeEmojis = {}
commandsEnabled = True
discordClassAttributesOverridesDict = {}
progressMessage = None
progressMessagePercentage = 0





virtualFiles = (

    {

        "bot.json": "{\"master\": 619798700675563530, \"authorisedUsers\": [619798700675563530, 403781691249917952, 276976462140014593], \"semiauthorisedUsers\": [821525100020367390], \"logFile\": \"C:\\\\Users\\\\MattL\\\\Documents\\\\visual studio projects\\\\test website\\\\bot\\\\log.txt\", \"logChannel\": 878847608506953738, \"streamingSettings\": {\"name\": \"| use \\\\?\", \"url\": \"https://www.twitch.tv/shardowyt_/about\"}, \"shortAutoclearTime\": null, \"longAutoclearTime\": null, \"maxDepth\": 3, \"allDataAttributes\": {}, \"attributeMaxLength\": 2048, \"deleteMessages\": true, \"validCommands\": {\"commands\": [\"hellp\", \"easteregg\", \"hi\", \"hey\", \"helo\", \"hello\", \"hullo\", \"ara\", \"owo\", \"uwu\", \"snow\", \"snowy\", \"snowflake\", \"?\", \"help\", \"rng\", \"random\", \"ut\", \"uptime\", \"at\", \"atd\", \"atf\", \"gfl\", \"autofill\", \"autofiller\", \"tl\", \"timetablelinks\", \"pp\", \"prettyprint\", \"ie\", \"ifempty\", \"iz\", \"ifzero\", \"in\", \"iflength\", \"it\", \"iftrue\", \"ig\", \"ifgreater\", \"il\", \"ifless\", \"igl\", \"ifgreaterless\", \"wi\", \"whileiter\", \"fi\", \"foriter\", \"di\", \"dictiter\", \"gh\", \"gethistory\", \"pf\", \"parsefile\", \"svrinfo\", \"cl\", \"clear\", \"et\", \"emergencytimetable\", \"rs\", \"removeSmirk\", \"dc\", \"deletecall\", \"ws\", \"writesettings\", \"la\", \"listattributes\", \"ss\", \"setstatus\", \"ri\", \"rebuildindex\", \"cc\", \"commander\", \"co\", \"operator\", \"rt\", \"ping\", \"?ack\", \"?acknowledgements\", \"ls\", \"cat\", \"nano\", \"owoify\", \"listen\", \"ignore\", \"terminate\", \"say\", \"rai\", \"adl\", \"jv\", \"joinvoice\"], \"replies\": {\"hellp\": \"trollHelpEmbed\", \"egg\": \"eggEmoji\", \"easteregg\": \"eggEmoji\", \"hi\": \"handEmoji\", \"hey\": \"handEmoji\", \"helo\": \"handEmoji\", \"hello\": \"handEmoji\", \"hullo\": \"handEmoji\", \"ara\": \"why\", \"owo\": \"why\", \"uwu\": \"why\", \"snow\": \"snowflakeEmoji\", \"snowy\": \"snowflakeEmoji\", \"snowflake\": \"snowflakeEmoji\", \"?\": \"helpEmbed\", \"help\": \"helpEmbed\", \"rng\": \"randomNumber\", \"random\": \"randomNumber\", \"ut\": \"upTime\", \"uptime\": \"upTime\", \"at\": \"attendanceEmbed\", \"atd\": \"attendanceEmbed\", \"atf\": \"attendanceEmbed\", \"gfl\": \"attendanceEmbed\", \"autofill\": \"attendanceEmbed\", \"autofiller\": \"attendanceEmbed\", \"tl\": \"getTimetables\", \"timetablelinks\": \"getTimetables\", \"pp\": \"prettyPrint\", \"prettyprint\": \"prettyPrint\", \"ie\": \"ifEmptyCodeBlock\", \"ifempty\": \"ifEmptyCodeBlock\", \"iz\": \"ifZeroCodeBlock\", \"ifzero\": \"ifZeroCodeBlock\", \"in\": \"ifLongCodeBlock\", \"iflength\": \"ifLongCodeBlock\", \"it\": \"ifTrueCodeBlock\", \"iftrue\": \"ifTrueCodeBlock\", \"ig\": \"ifGreaterCodeBlock\", \"ifgreater\": \"ifGreaterCodeBlock\", \"il\": \"ifLessCodeBlock\", \"ifless\": \"ifLessCodeBlock\", \"igl\": \"ifGreaterLessCodeBlock\", \"ifgreaterless\": \"ifGreaterLessCodeBlock\", \"fi\": \"forIteratorCodeBlock\", \"foriter\": \"forIteratorCodeBlock\", \"wi\": \"whileIteratorCodeBlock\", \"whileiter\": \"whileIteratorCodeBlock\", \"di\": \"dictionaryIteratorCodeBlock\", \"dictiter\": \"dictionaryIteratorCodeBlock\", \"pf\": \"fileCodeBlock\", \"parsefile\": \"fileCodeBlock\", \"gh\": \"getHistory\", \"gethistory\": \"getHistory\", \"cl\": \"autoClear\", \"clear\": \"autoClear\", \"et\": \"generateTimetable\", \"emergencytimetable\": \"generateTimetable\", \"rs\": \"removeSmirk\", \"removeSmirk\": \"removeSmirk\", \"dc\": \"deleteCallingMessage\", \"deletecall\": \"deleteCallingMessage\", \"ws\": \"writeSettings\", \"writesettings\": \"writeSettings\", \"la\": \"listAttributes\", \"listattributes\": \"listAttributes\", \"ss\": \"setStatus\", \"setstatus\": \"setStatus\", \"ri\": \"rebuildIndex\", \"rebuildindex\": \"rebuildIndex\", \"cc\": \"checkForCommander\", \"commander\": \"checkForCommander\", \"co\": \"checkForOperator\", \"operator\": \"checkForOperator\", \"rt\": \"testPing\", \"ping\": \"testPing\", \"?ack\": \"acknowledgementsHelpEmbed\", \"?acknowledgements\": \"acknowledgementsHelpEmbed\", \"ls\": \"ls\", \"cat\": \"cat\", \"nano\": \"nano\", \"owoify\": \"owoify\", \"listen\": \"startListening\", \"ignore\": \"stopListening\", \"terminate\": \"terminate\", \"say\": \"copyUserText\", \"rai\": \"revokeAllInvites\", \"adl\": \"addListeners\", \"jv\": \"joinVoice\", \"joinvoice\": \"joinVoice\"}}, \"defaultStatus\": \"streaming\", \"serverSettings\": {\"877157413168484432\": {\"deleteCalls\": true}, \"692688320706379777\": {\"deleteCalls\": false}}, \"typeEmojis\": {\"string\": \"883155569869979658\", \"dictionary\": \"883155570029387786\", \"float\": \"883155569911930960\", \"boolean\": \"883155569890971708\", \"snowflakeid\": \"883155569958092800\", \"integer\": \"883155569710608406\"}, \"helpEmojis\": {\"home\": \"882810562126417930\", \"restricted\": \"882810562214518835\", \"automated\": \"915861328235757599\", \"code\": \"882810561690222613\", \"symbols\": \"882810561786699817\", \"acknowledgements\": \"882810562055131186\"}, \"reactionsEnabled\": true, \"classOverrides\": {\"Guild\": [\"afk_channel.id\", \"afk_timeout\", \"banner\", \"banner_url\", \"bitrate_limit\", \"default_notifications\", \"default_role.id\", \"description\", \"discovery_splash\", \"discovery_splash_url\", \"emoji_limit\", \"emojis\", \"explicit_content_filter\", \"features\", \"filesize_limit\", \"icon\", \"icon_url\", \"id\", \"max_members\", \"max_presences\", \"max_video_channel_users\", \"member_count\", \"members\", \"mfa_level\", \"name\", \"owner_id\", \"preferred_locale\", \"premium_subscriber_role\", \"premium_subscribers\", \"premium_subscription_count\", \"public_updates_channel.id\", \"region\", \"rules_channel.id\", \"shard_id\", \"splash\", \"splash_url\", \"system_channel.id\", \"system_channel_flags\", \"verification_level\"], \"Message\": [\"id\", \"author.id\", \"edited_at\", \"content\", \"embeds\", \"attachments\", \"reference\", \"pinned\", \"stickers\", \"reactions\"], \"CategoryChannel\": [\"category\", \"changed_roles\", \"created_at\", \"id\", \"name\", \"overwrites\", \"permissions_synced\", \"position\", \"stage_channels\", \"text_channels\", \"type\", \"voice_channels\"], \"DMChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"GroupChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"StageChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"StoreChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"TextChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"VoiceChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"PartialInviteChannel\": [\"bitrate\", \"changed_roles\", \"created_at\", \"id\", \"members\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"slowmode_delay\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"Role\": [\"color\", \"hoist\", \"id\", \"managed\", \"mentionable\", \"name\", \"permissions\", \"position\", \"tags\"], \"Colour\": [\"value\"], \"ChannelType\": [\"category\", \"group\", \"news\", \"private\", \"stage_voice\", \"store\", \"text\", \"voice\"], \"PermissionOverwrite\": [\"PURE_FLAGS\", \"VALID_NAMES\", \"add_reactions\", \"administrator\", \"attach_files\", \"ban_members\", \"change_nickname\", \"connect\", \"create_instant_invite\", \"deafen_members\", \"embed_links\", \"external_emojis\", \"kick_members\", \"manage_channels\", \"manage_emojis\", \"manage_guild\", \"manage_messages\", \"manage_nicknames\", \"manage_permissions\", \"manage_roles\", \"manage_webhooks\", \"mention_everyone\", \"move_members\", \"mute_members\", \"priority_speaker\", \"read_message_history\", \"read_messages\", \"request_to_speak\", \"send_messages\", \"send_tts_messages\", \"speak\", \"stream\", \"use_external_emojis\", \"use_slash_commands\", \"use_voice_activation\", \"view_audit_log\", \"view_channel\", \"view_guild_insights\"], \"Permissions\": [\"value\"], \"Embed\": [\"author\", \"colour\", \"description\", \"fields\", \"footer\", \"image\", \"provider\", \"thumbnail\", \"timestamp\", \"title\", \"type\", \"url\", \"video\", \"to_dict()\"], \"Attachment\": [\"filename\", \"id\", \"url\", \"is_spoiler()\"], \"MessageReference\": [\"message_id\"], \"Member\": [\"activities\", \"avatar_url\", \"bot\", \"desktop_status\", \"discriminator\", \"display_name\", \"dm_channel\", \"guild\", \"id\", \"mobile_status\", \"name\", \"nick\", \"pending\", \"premium_since\", \"public_flags\", \"raw_status\", \"relationship\", \"roles\", \"status\", \"system\", \"voice\", \"web_status\"], \"Emoji\": [\"animated\", \"available\", \"id\", \"managed\", \"name\", \"require_colons\", \"roles\", \"url\", \"user\"]}, \"classOverridesOverrides\": {\"Activity\": [], \"ActivityType\": [], \"AllowedMentions\": [], \"AppInfo\": [\"id\"], \"Asset\": [], \"AsyncWebhookAdapter\": [], \"Attachment\": [\"id\"], \"AudioSource\": [], \"AuditLogAction\": [], \"AuditLogActionCategory\": [], \"AuditLogChanges\": [], \"AuditLogDiff\": [], \"AuditLogEntry\": [], \"AutoShardedClient\": [], \"BaseActivity\": [], \"CallMessage\": [], \"CategoryChannel\": [\"id\"], \"ChannelType\": [\"category\", \"group\", \"news\", \"private\", \"stage_voice\", \"store\", \"text\", \"voice\"], \"Client\": [], \"ClientException\": [], \"ClientUser\": [\"id\"], \"Colour\": [\"value\"], \"ConnectionClosed\": [], \"ContentFilter\": [], \"CustomActivity\": [], \"DMChannel\": [\"id\"], \"DefaultAvatar\": [], \"DeletedReferencedMessage\": [\"id\"], \"DiscordException\": [], \"DiscordServerError\": [], \"Embed\": [], \"Emoji\": [\"id\"], \"Enum\": [], \"ExpireBehaviour\": [], \"FFmpegAudio\": [], \"FFmpegOpusAudio\": [], \"FFmpegPCMAudio\": [], \"File\": [], \"Forbidden\": [], \"FriendFlags\": [], \"Game\": [], \"GatewayNotFound\": [], \"GroupCall\": [], \"GroupChannel\": [\"id\"], \"Guild\": [\"id\"], \"HTTPException\": [], \"HypeSquadHouse\": [], \"Integration\": [\"id\"], \"IntegrationAccount\": [\"id\"], \"Intents\": [], \"InvalidArgument\": [], \"InvalidData\": [], \"Invite\": [\"id\"], \"LoginFailure\": [], \"Member\": [\"id\"], \"MemberCacheFlags\": [], \"Message\": [\"id\"], \"MessageFlags\": [], \"MessageReference\": [], \"MessageType\": [], \"NoMoreItems\": [], \"NotFound\": [], \"NotificationLevel\": [], \"Object\": [], \"PCMAudio\": [], \"PCMVolumeTransformer\": [], \"PartialEmoji\": [\"id\"], \"PartialInviteChannel\": [\"id\"], \"PartialInviteGuild\": [\"id\"], \"PartialMessage\": [\"id\"], \"PermissionOverwrite\": [], \"Permissions\": [\"value\"], \"PremiumType\": [], \"PrivilegedIntentsRequired\": [], \"Profile\": [], \"PublicUserFlags\": [], \"RawBulkMessageDeleteEvent\": [], \"RawMessageDeleteEvent\": [], \"RawMessageUpdateEvent\": [], \"RawReactionActionEvent\": [], \"RawReactionClearEmojiEvent\": [], \"RawReactionClearEvent\": [], \"Reaction\": [], \"Relationship\": [], \"RelationshipType\": [], \"RequestsWebhookAdapter\": [], \"Role\": [\"id\"], \"RoleTags\": [], \"ShardInfo\": [\"id\"], \"SpeakingState\": [], \"Spotify\": [], \"StageChannel\": [\"id\"], \"Status\": [], \"Sticker\": [\"id\"], \"StickerType\": [], \"StoreChannel\": [\"id\"], \"Streaming\": [], \"SystemChannelFlags\": [], \"Team\": [\"id\"], \"TeamMember\": [\"id\"], \"TeamMembershipState\": [], \"Template\": [], \"TextChannel\": [\"id\"], \"Theme\": [], \"User\": [\"id\"], \"UserContentFilter\": [], \"UserFlags\": [], \"VerificationLevel\": [], \"VersionInfo\": [], \"VoiceChannel\": [\"id\"], \"VoiceClient\": [], \"VoiceProtocol\": [], \"VoiceRegion\": [], \"VoiceState\": [], \"Webhook\": [\"id\"], \"WebhookAdapter\": [], \"WebhookMessage\": [\"id\"], \"WebhookType\": [], \"Widget\": [\"id\"], \"WidgetChannel\": [\"id\"], \"WidgetMember\": [\"id\"]}}",
        "metainfo.json": "{\"acknowledgementsHelpEmbed\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Acknowlegements)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"A list of third-party licenses\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Third-party licenses\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Material Icons\", \"value\": \"[__License__](https://raw.githubusercontent.com/google/material-design-icons/master/LICENSE)\", \"inline\": true}, {\"name\": \"*Random note*\", \"value\": \"\\u2bc7 somehow google was so lazy they didnt apply the license properly and put `Copyright [yyyy] [name of copyright owner]` instead of the correct identifying information\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"symbolKeyHelpEmbed\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Symbols)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"A key to symbols used\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Symbols used\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"string $string$\", \"value\": \"__Allowed values:__\\n*any sequence of characters*\\n`bots are cool`\", \"inline\": true}, {\"name\": \"identifier $snowflakeid$\", \"value\": \"__Allowed values:__\\n*any valid snowflake id*\\n`4581042757`\", \"inline\": true}, {\"name\": \"json $dictionary$\", \"value\": \"__Allowed values:__\\n*any valid json*\\n`{\\\"variables\\\": [\\n\\\"foo\\\", \\\"bar\\\"]}`\", \"inline\": true}, {\"name\": \"integer $integer$\", \"value\": \"__Allowed values:__\\n*any whole number*\\n`14`\", \"inline\": true}, {\"name\": \"float $float$\", \"value\": \"__Allowed values:__\\n*any number*\\n`61.07734`\", \"inline\": true}, {\"name\": \"boolean $boolean$\", \"value\": \"__Allowed values:__\\n*any boolean value*\\n`true|1|=|+|on|yes`\\n`false|0|-|off|no`\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"helpMenu\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Normal)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"commands are not case sensitive\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Normal Commands\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"\\\\\\\\?|help\", \"value\": \"shows the help embed\", \"inline\": true}, {\"name\": \"\\\\hi|hey|helo|hello|hullo\", \"value\": \"replies with a wave\", \"inline\": true}, {\"name\": \"\\\\rng|random <$integer$start> <$integer$end>\", \"value\": \"generates a random integer between the two integers specified (inclusive)\", \"inline\": false}, {\"name\": \"\\\\tl|timetablelinks\", \"value\": \"lists available manual timetable links\", \"inline\": true}, {\"name\": \"\\\\at|atd|atf|gfl|autofill|autofiller\", \"value\": \"lists available customised timetable tokens\", \"inline\": true}, {\"name\": \"\\\\rt|ping\", \"value\": \"tests the round trip time (~400ms)\", \"inline\": true}, {\"name\": \"\\\\cc|commander\", \"value\": \"checks if the author is a commander\", \"inline\": true}, {\"name\": \"\\\\co|operator\", \"value\": \"checks if the author is an operator\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"restrictedHelpMenu\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Restricted)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"commands are not case sensitive\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Restricted Commands\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"\\\\gh|gethistory <$string$message|server|channel|role|member|emoji> <$boolean$condensed> <$boolean$collapsed> <$integer$searchlimit> <$integer$depth>\", \"value\": \"fetches the specified data\", \"inline\": true}, {\"name\": \"\\\\dc|deletecall <$boolean$enabled>\", \"value\": \"deletes calling messages after a period of time\", \"inline\": true}, {\"name\": \"\\\\et|emergencytimetable\", \"value\": \"emulates Snowy Bot's timetable ping (only once)\", \"inline\": false}, {\"name\": \"\\\\cl|clear <$integer$searchlimit>\", \"value\": \"clears messages sent by 'shardow-1' within a specified number of messages\", \"inline\": true}, {\"name\": \"\\\\rs|removesmirk <$integer$userid> <$integer$searchlimit>\", \"value\": \"removes that smirk from ~~*that users face*~~ your messages\", \"inline\": true}, {\"name\": \"\\\\ss|setstatus <$string$schedule|streaming|competing|online|idle|dnd|invisible>, \\\"<$string$status>\\\"\", \"value\": \"set the presence of 'shardow-1'\", \"inline\": false}, {\"name\": \"\\\\listen\", \"value\": \"enables the usage of commands\", \"inline\": true}, {\"name\": \"\\\\ignore\", \"value\": \"disables the usage of commands\", \"inline\": true}, {\"name\": \"\\\\terminate\", \"value\": \"stops 'shardow-1'\", \"inline\": true}, {\"name\": \"\\\\ri|rebuildindex\", \"value\": \"rebuilds the list of class attributes of discord.py\", \"inline\": true}, {\"name\": \"\\\\la|listattributes\", \"value\": \"lists all class attributes of discord.py\", \"inline\": true}, {\"name\": \"\\\\say <$string$text>\", \"value\": \"copies your message\", \"inline\": true}, {\"name\": \"\\\\ut|uptime\", \"value\": \"shows the uptime\", \"inline\": true}, {\"name\": \"\\\\rai\", \"value\": \"revokes all invites\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"automatedHelpMenu\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Unstable)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"commands are not case sensitive\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Unstable Commands\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"register verification in <$snowflakeid$channel> logging to <$snowflakeid$channel> requiring <$snowflakeid$roles> applying <$snowflakeid$roles>\", \"value\": \"enables verification of users\", \"inline\": false}, {\"name\": \"unregister verification in <$snowflakeid$channel>\", \"value\": \"disables verification of users\", \"inline\": false}, {\"name\": \"register mentions logging to <$snowflakeid$channel>\", \"value\": \"enables mention logging\", \"inline\": false}, {\"name\": \"unregister mentions logging\", \"value\": \"disables mention logging\", \"inline\": true}, {\"name\": \"rep /<$string$regex>/, <$integer$searchlimit>\", \"value\": \"searches for messages containing text matching the specified pattern\", \"inline\": false}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"iteratorHelpMenu\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Code Blocks)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"commands are not case sensitive\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Code Block Commands\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"\\\\pp|prettyprint <$dictionary$json>\", \"value\": \"pretty-prints JSON files\\n\\u200b\", \"inline\": false}, {\"name\": \"\\\\ie|ifempty <$string$variable>\", \"value\": \"prints an if-elif empty block\", \"inline\": true}, {\"name\": \"\\\\iz|ifzero <$string$variable>\", \"value\": \"prints an if-elif zero block\", \"inline\": true}, {\"name\": \"\\\\in|iflength <$string$variable>\", \"value\": \"prints an if-elif length block\", \"inline\": true}, {\"name\": \"\\\\ig|ifgreater <$string$variable> <$integer$size>\", \"value\": \"prints an if-elif greater than block\", \"inline\": true}, {\"name\": \"\\\\il|ifless <$string$variable> <$integer$size>\", \"value\": \"prints an if-elif less than block\", \"inline\": true}, {\"name\": \"\\\\igl|ifgreaterless <$string$variable> <$integer$minsize> <$integer$maxsize>\", \"value\": \"prints an if-elif less and greater than block\", \"inline\": true}, {\"name\": \"\\\\fi|foriter <$string$variable>\", \"value\": \"prints a for iterator block\", \"inline\": true}, {\"name\": \"\\\\wi|whileiter <$string$variable>\", \"value\": \"prints an while iterator block\", \"inline\": true}, {\"name\": \"\\\\di|dictiter <$string$variable>\", \"value\": \"prints an dictionary iterator block\", \"inline\": true}, {\"name\": \"\\\\it|iftrue <$string$variable>\", \"value\": \"prints an if-elif true block\", \"inline\": true}, {\"name\": \"\\\\pf|parsefile <$string$variable>\", \"value\": \"prints an json-parsing block\\n\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"undocumentedHelpMenu\": [{\"title\": \"\", \"url\": \"\", \"description\": \"*commands are not case sensitive*\", \"color\": 8388800}, {\"name\": \"SHArdow-1 Help Page (Undocumented)\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"commands are not case sensitive\"}, [{\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Undocumented Commands\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"\\\\owoify <$string$text>\", \"value\": \"??\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u2001\\u200b\", \"inline\": false}]], \"timetables\": [{\"title\": \"Timetable Links\", \"url\": \"\", \"description\": \"A list of auto-filled timetables\\n\\u200b\", \"color\": 8437760}, {\"name\": \"\", \"url\": \"\", \"icon_url\": \"\"}, {\"text\": \"dm shardow if you have a suggestion\"}, [{\"name\": \"Normal Forms\", \"value\": \"use `\\\\tl|timetablelinks` instead\", \"inline\": false}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Custom Forms\", \"value\": \"go to\\u2001\\u2001https://shardowyt.github.io/public/\\u2001\\u2001and input your token\\n\\u200b\", \"inline\": false}, {\"name\": \"\\u200b\", \"value\": \"***dank_nightfury.exe***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      442aa149cd84c259f80a35279edeec12      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***james.***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      1d25c1cf69f2ff1ab9921c1756d1ec88      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***Tranquilifier***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      0c86b4781b843a27f0e9252818854d6b      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***TooTHleZZ***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\\n\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      861571ff0347b8d69a906af7c9bf0e47      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***Year 9 (Gamma)***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      fbd0017d663899c680f79f311bb3dd57      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***Year 9 (Beta)***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      2cfd8b7c75ce948c22378aa01e8a84a1      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"***Year 9 (Alpha)***\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"`      958d3d815204303031be651e89d52176      `\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}]], \"forms\": [{\"title\": \"Timetable Links\", \"url\": \"\", \"description\": \"A list of manual timetable links\\n\\u200b\", \"color\": 32960}, {\"name\": \"\", \"url\": \"\", \"icon_url\": \"\"}, {\"text\": \"dm shardow if you have a suggestion\"}, [{\"name\": \"Normal Forms\\n\\u200b\", \"value\": \"[Year 7 Form](https://docs.google.com/forms/d/e/1FAIpQLSf0wNsk9bJF9VxF-gZ7DAN6hvov3vr1EFHZrMyRk0WRQ_m8bA/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\\n\\u200b\", \"value\": \"[Year 9 Form](https://docs.google.com/forms/d/e/1FAIpQLSc1aXXrENpHmaJ30zlmR4xWnNv6mRw4jKJSiZeUErAG9e6bdw/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\\n\\u200b\", \"value\": \"[Year 11 Form](https://docs.google.com/forms/d/e/1FAIpQLScVR8KK7CPhdcbgg0CkpCNEofQEKy0h8uyw0JCFsPPh0EJFhg/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"[Year 8 Form](https://docs.google.com/forms/d/e/1FAIpQLSdBn_QwHom86htHoZYGuG6YjXTvjL_-IJoCdoiYMVVbZMwU9g/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"[Year 10 Form](https://docs.google.com/forms/d/e/1FAIpQLSew3K82Uj9SRrtd0C1wHyC4Rn9neUmOCy1AzcCz7tRYJzFHGw/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"[Year 12 Form](https://docs.google.com/forms/d/e/1FAIpQLSdqg7NnSAYiZjIafsTDwsaemF1ZRmBNi4yP5uYxEw5f0O0d6A/viewform)\", \"inline\": true}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}, {\"name\": \"Custom Forms\", \"value\": \"use `\\\\at|atd|atf|gfl|autofill|autofiller` instead\", \"inline\": false}, {\"name\": \"\\u200b\", \"value\": \"\\u200b\", \"inline\": false}]], \"commanderYes\": [{\"title\": \"**Yes**\", \"url\": \"\", \"description\": \"*you __are__ a commander*\", \"color\": 8437760}, {\"name\": \"SHArdow-1 Commander Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"commanderNo\": [{\"title\": \"**No**\", \"url\": \"\", \"description\": \"*you __are not__ a commander*\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Commander Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"operatorCommanderYes\": [{\"title\": \"**Yes [you are a commander]**\", \"url\": \"\", \"description\": \"*you __are__ an operator (and commander)*\", \"color\": 16760832}, {\"name\": \"SHArdow-1 Operator Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"operatorYes\": [{\"title\": \"**Yes**\", \"url\": \"\", \"description\": \"*you __are__ an operator*\", \"color\": 8437760}, {\"name\": \"SHArdow-1 Operator Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"operatorNo\": [{\"title\": \"**No**\", \"url\": \"\", \"description\": \"*you __are not__ an operator*\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Operator Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"randomNumber\": [{\"title\": \"Random Number Generator\", \"url\": \"\", \"description\": \"**Result:** `    -1    `\", \"color\": 16760832}, {\"name\": \"SHArdow-1 RandInt Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"uptime\": [{\"title\": \"Time since start\", \"url\": \"\", \"description\": \"Time: `0:00:00`\", \"color\": 16760832}, {\"name\": \"SHArdow-1 Uptime Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"roundTripTime\": [{\"title\": \"Round Trip Time\", \"url\": \"\", \"description\": \"Time: `0 ms`\", \"color\": 16760832}, {\"name\": \"SHArdow-1 Roundtrip Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"taskCompleted\": [{\"title\": \"Completed!\", \"url\": \"\", \"description\": \" \", \"color\": 8437760}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"taskDisabled\": [{\"title\": \"Failed to run!\", \"url\": \"\", \"description\": \" \", \"color\": 12582912}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"taskCooling\": [{\"title\": \"Command cooling down!\", \"url\": \"\", \"description\": \" \", \"color\": 16760832}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"unspecifiedParameters\": [{\"title\": \"Error: Parameters are not fully specified\", \"url\": \"\", \"description\": \"\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"invalidParameters\": [{\"title\": \"Error: Parameters provided are invalid\", \"url\": \"\", \"description\": \"\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"unauthorisedUser\": [{\"title\": \"Error: Unauthorised user\", \"url\": \"\", \"description\": \"\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"notImplemented\": [{\"title\": \"This function is not implemented!\", \"url\": \"\", \"description\": \"\", \"color\": 16760832}, {\"name\": \"\", \"url\": \"\", \"icon_url\": \"\"}, {\"text\": \"\"}, []], \"timetable\": [{\"title\": \"Current Period\", \"url\": \"\", \"description\": \"\", \"color\": 16760832}, {\"name\": \"SHArdow-1 Period Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"commandDisabled\": [{\"title\": \"Error: Command disabled\", \"url\": \"\", \"description\": \"\", \"color\": 12582912}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []], \"userVerified\": [{\"title\": \"Verified!\", \"url\": \"\", \"description\": \" \", \"color\": 8437760}, {\"name\": \"SHArdow-1 Miscellaneous Query\", \"url\": \"\", \"icon_url\": \"https://cdn.discordapp.com/attachments/882810612277731400/926433125406490664/image0.png\"}, {\"text\": \"\"}, []]}",
        "index.json": "{\"discordClassNameAttributesDict\": {\"Activity\": [\"application_id\", \"assets\", \"created_at\", \"details\", \"emoji\", \"end\", \"flags\", \"large_image_text\", \"large_image_url\", \"name\", \"party\", \"session_id\", \"small_image_text\", \"small_image_url\", \"start\", \"state\", \"sync_id\", \"timestamps\", \"type\", \"url\"], \"ActivityType\": [\"competing\", \"custom\", \"listening\", \"playing\", \"streaming\", \"unknown\", \"watching\"], \"AllowedMentions\": [\"everyone\", \"replied_user\", \"roles\", \"users\"], \"AppInfo\": [\"bot_public\", \"bot_require_code_grant\", \"cover_image\", \"cover_image_url\", \"description\", \"guild\", \"guild_id\", \"icon\", \"icon_url\", \"id\", \"name\", \"owner\", \"primary_sku_id\", \"rpc_origins\", \"slug\", \"summary\", \"team\", \"verify_key\"], \"Asset\": [\"BASE\"], \"AsyncWebhookAdapter\": [\"BASE\"], \"Attachment\": [\"content_type\", \"filename\", \"height\", \"id\", \"proxy_url\", \"size\", \"url\", \"width\"], \"AudioSource\": [], \"AuditLogAction\": [\"ban\", \"bot_add\", \"channel_create\", \"channel_delete\", \"channel_update\", \"emoji_create\", \"emoji_delete\", \"emoji_update\", \"guild_update\", \"integration_create\", \"integration_delete\", \"integration_update\", \"invite_create\", \"invite_delete\", \"invite_update\", \"kick\", \"member_disconnect\", \"member_move\", \"member_prune\", \"member_role_update\", \"member_update\", \"message_bulk_delete\", \"message_delete\", \"message_pin\", \"message_unpin\", \"overwrite_create\", \"overwrite_delete\", \"overwrite_update\", \"role_create\", \"role_delete\", \"role_update\", \"unban\", \"webhook_create\", \"webhook_delete\", \"webhook_update\"], \"AuditLogActionCategory\": [\"create\", \"delete\", \"update\"], \"AuditLogChanges\": [\"TRANSFORMERS\"], \"AuditLogDiff\": [], \"AuditLogEntry\": [\"after\", \"before\", \"category\", \"changes\", \"created_at\", \"target\"], \"AutoShardedClient\": [\"activity\", \"allowed_mentions\", \"cached_messages\", \"emojis\", \"guilds\", \"intents\", \"latencies\", \"latency\", \"private_channels\", \"shards\", \"user\", \"users\", \"voice_clients\"], \"BaseActivity\": [\"created_at\"], \"CallMessage\": [\"call_ended\", \"channel\", \"duration\"], \"CategoryChannel\": [\"category\", \"category_id\", \"changed_roles\", \"channels\", \"created_at\", \"guild\", \"id\", \"mention\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"stage_channels\", \"text_channels\", \"type\", \"voice_channels\"], \"ChannelType\": [\"category\", \"group\", \"news\", \"private\", \"stage_voice\", \"store\", \"text\", \"voice\"], \"Client\": [\"activity\", \"allowed_mentions\", \"cached_messages\", \"emojis\", \"guilds\", \"intents\", \"latency\", \"private_channels\", \"user\", \"users\", \"voice_clients\"], \"ClientException\": [\"args\", \"with_traceback\"], \"ClientUser\": [\"avatar\", \"avatar_url\", \"blocked\", \"bot\", \"color\", \"colour\", \"created_at\", \"default_avatar\", \"default_avatar_url\", \"discriminator\", \"display_name\", \"email\", \"friends\", \"id\", \"locale\", \"mention\", \"mfa_enabled\", \"name\", \"premium\", \"premium_type\", \"public_flags\", \"relationships\", \"system\", \"verified\"], \"Colour\": [\"b\", \"g\", \"r\", \"value\"], \"ConnectionClosed\": [\"args\", \"with_traceback\"], \"ContentFilter\": [\"all_members\", \"disabled\", \"no_role\"], \"CustomActivity\": [\"created_at\", \"emoji\", \"name\", \"state\", \"type\"], \"DMChannel\": [\"created_at\", \"id\", \"me\", \"recipient\", \"type\"], \"DefaultAvatar\": [\"blurple\", \"gray\", \"green\", \"grey\", \"orange\", \"red\"], \"DeletedReferencedMessage\": [\"channel_id\", \"guild_id\", \"id\"], \"DiscordException\": [\"args\", \"with_traceback\"], \"DiscordServerError\": [\"args\", \"with_traceback\"], \"Embed\": [\"Empty\", \"author\", \"color\", \"colour\", \"description\", \"fields\", \"footer\", \"image\", \"provider\", \"thumbnail\", \"timestamp\", \"title\", \"type\", \"url\", \"video\"], \"Emoji\": [\"animated\", \"available\", \"created_at\", \"guild\", \"guild_id\", \"id\", \"managed\", \"name\", \"require_colons\", \"roles\", \"url\", \"user\"], \"Enum\": [], \"ExpireBehaviour\": [\"kick\", \"remove_role\"], \"FFmpegAudio\": [], \"FFmpegOpusAudio\": [], \"FFmpegPCMAudio\": [], \"File\": [\"filename\", \"fp\", \"spoiler\"], \"Forbidden\": [\"args\", \"with_traceback\"], \"FriendFlags\": [\"everyone\", \"guild_and_friends\", \"mutual_friends\", \"mutual_guilds\", \"noone\"], \"Game\": [\"created_at\", \"end\", \"name\", \"start\", \"type\"], \"GatewayNotFound\": [\"args\", \"with_traceback\"], \"GroupCall\": [\"channel\", \"connected\"], \"GroupChannel\": [\"created_at\", \"icon\", \"icon_url\", \"id\", \"me\", \"name\", \"owner\", \"recipients\", \"type\"], \"Guild\": [\"afk_channel\", \"afk_timeout\", \"banner\", \"banner_url\", \"bitrate_limit\", \"categories\", \"channels\", \"chunked\", \"created_at\", \"default_notifications\", \"default_role\", \"description\", \"discovery_splash\", \"discovery_splash_url\", \"emoji_limit\", \"emojis\", \"explicit_content_filter\", \"features\", \"filesize_limit\", \"icon\", \"icon_url\", \"id\", \"large\", \"max_members\", \"max_presences\", \"max_video_channel_users\", \"me\", \"member_count\", \"members\", \"mfa_level\", \"name\", \"owner\", \"owner_id\", \"preferred_locale\", \"premium_subscriber_role\", \"premium_subscribers\", \"premium_subscription_count\", \"premium_tier\", \"public_updates_channel\", \"region\", \"roles\", \"rules_channel\", \"self_role\", \"shard_id\", \"splash\", \"splash_url\", \"stage_channels\", \"system_channel\", \"system_channel_flags\", \"text_channels\", \"unavailable\", \"verification_level\", \"voice_channels\", \"voice_client\"], \"HTTPException\": [\"args\", \"with_traceback\"], \"HypeSquadHouse\": [\"balance\", \"bravery\", \"brilliance\"], \"Integration\": [\"account\", \"enable_emoticons\", \"enabled\", \"expire_behavior\", \"expire_behaviour\", \"expire_grace_period\", \"guild\", \"id\", \"name\", \"role\", \"synced_at\", \"syncing\", \"type\", \"user\"], \"IntegrationAccount\": [\"id\", \"name\"], \"Intents\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"bans\", \"dm_messages\", \"dm_reactions\", \"dm_typing\", \"emojis\", \"guild_messages\", \"guild_reactions\", \"guild_typing\", \"guilds\", \"integrations\", \"invites\", \"members\", \"messages\", \"presences\", \"reactions\", \"typing\", \"value\", \"voice_states\", \"webhooks\"], \"InvalidArgument\": [\"args\", \"with_traceback\"], \"InvalidData\": [\"args\", \"with_traceback\"], \"Invite\": [\"BASE\", \"approximate_member_count\", \"approximate_presence_count\", \"channel\", \"code\", \"created_at\", \"guild\", \"id\", \"inviter\", \"max_age\", \"max_uses\", \"revoked\", \"temporary\", \"url\", \"uses\"], \"LoginFailure\": [\"args\", \"with_traceback\"], \"Member\": [\"activities\", \"activity\", \"avatar\", \"avatar_url\", \"bot\", \"color\", \"colour\", \"created_at\", \"default_avatar\", \"default_avatar_url\", \"desktop_status\", \"discriminator\", \"display_name\", \"dm_channel\", \"guild\", \"guild_permissions\", \"id\", \"joined_at\", \"mention\", \"mobile_status\", \"mutual_guilds\", \"name\", \"nick\", \"pending\", \"premium_since\", \"public_flags\", \"raw_status\", \"relationship\", \"roles\", \"status\", \"system\", \"top_role\", \"voice\", \"web_status\"], \"MemberCacheFlags\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"joined\", \"online\", \"value\", \"voice\"], \"Message\": [\"activity\", \"application\", \"attachments\", \"author\", \"call\", \"channel\", \"channel_mentions\", \"clean_content\", \"content\", \"created_at\", \"edited_at\", \"embeds\", \"flags\", \"guild\", \"id\", \"jump_url\", \"mention_everyone\", \"mentions\", \"nonce\", \"pinned\", \"raw_channel_mentions\", \"raw_mentions\", \"raw_role_mentions\", \"reactions\", \"reference\", \"role_mentions\", \"stickers\", \"system_content\", \"tts\", \"type\", \"webhook_id\"], \"MessageFlags\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"crossposted\", \"is_crossposted\", \"source_message_deleted\", \"suppress_embeds\", \"urgent\", \"value\"], \"MessageReference\": [\"cached_message\", \"channel_id\", \"fail_if_not_exists\", \"guild_id\", \"jump_url\", \"message_id\", \"resolved\"], \"MessageType\": [\"call\", \"channel_follow_add\", \"channel_icon_change\", \"channel_name_change\", \"default\", \"guild_discovery_disqualified\", \"guild_discovery_grace_period_final_warning\", \"guild_discovery_grace_period_initial_warning\", \"guild_discovery_requalified\", \"guild_stream\", \"new_member\", \"pins_add\", \"premium_guild_subscription\", \"premium_guild_tier_1\", \"premium_guild_tier_2\", \"premium_guild_tier_3\", \"recipient_add\", \"recipient_remove\"], \"NoMoreItems\": [\"args\", \"with_traceback\"], \"NotFound\": [\"args\", \"with_traceback\"], \"NotificationLevel\": [\"all_messages\", \"only_mentions\"], \"Object\": [\"created_at\"], \"PCMAudio\": [], \"PCMVolumeTransformer\": [\"volume\"], \"PartialEmoji\": [\"animated\", \"created_at\", \"id\", \"name\", \"url\"], \"PartialInviteChannel\": [\"created_at\", \"id\", \"mention\", \"name\", \"type\"], \"PartialInviteGuild\": [\"banner\", \"banner_url\", \"created_at\", \"description\", \"features\", \"icon\", \"icon_url\", \"id\", \"name\", \"splash\", \"splash_url\", \"verification_level\"], \"PartialMessage\": [\"channel\", \"created_at\", \"guild\", \"id\", \"jump_url\", \"pinned\"], \"PermissionOverwrite\": [\"PURE_FLAGS\", \"VALID_NAMES\", \"add_reactions\", \"administrator\", \"attach_files\", \"ban_members\", \"change_nickname\", \"connect\", \"create_instant_invite\", \"deafen_members\", \"embed_links\", \"external_emojis\", \"kick_members\", \"manage_channels\", \"manage_emojis\", \"manage_guild\", \"manage_messages\", \"manage_nicknames\", \"manage_permissions\", \"manage_roles\", \"manage_webhooks\", \"mention_everyone\", \"move_members\", \"mute_members\", \"priority_speaker\", \"read_message_history\", \"read_messages\", \"request_to_speak\", \"send_messages\", \"send_tts_messages\", \"speak\", \"stream\", \"use_external_emojis\", \"use_slash_commands\", \"use_voice_activation\", \"view_audit_log\", \"view_channel\", \"view_guild_insights\"], \"Permissions\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"add_reactions\", \"administrator\", \"attach_files\", \"ban_members\", \"change_nickname\", \"connect\", \"create_instant_invite\", \"deafen_members\", \"embed_links\", \"external_emojis\", \"kick_members\", \"manage_channels\", \"manage_emojis\", \"manage_guild\", \"manage_messages\", \"manage_nicknames\", \"manage_permissions\", \"manage_roles\", \"manage_webhooks\", \"mention_everyone\", \"move_members\", \"mute_members\", \"priority_speaker\", \"read_message_history\", \"read_messages\", \"request_to_speak\", \"send_messages\", \"send_tts_messages\", \"speak\", \"stream\", \"use_external_emojis\", \"use_slash_commands\", \"use_voice_activation\", \"value\", \"view_audit_log\", \"view_channel\", \"view_guild_insights\"], \"PremiumType\": [\"nitro\", \"nitro_classic\"], \"PrivilegedIntentsRequired\": [\"args\", \"with_traceback\"], \"Profile\": [\"bug_hunter\", \"connected_accounts\", \"count\", \"early_supporter\", \"flags\", \"hypesquad\", \"hypesquad_houses\", \"index\", \"mutual_guilds\", \"nitro\", \"partner\", \"premium\", \"premium_since\", \"staff\", \"system\", \"team_user\", \"user\"], \"PublicUserFlags\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"bug_hunter\", \"bug_hunter_level_2\", \"early_supporter\", \"early_verified_bot_developer\", \"hypesquad\", \"hypesquad_balance\", \"hypesquad_bravery\", \"hypesquad_brilliance\", \"partner\", \"staff\", \"system\", \"team_user\", \"value\", \"verified_bot\", \"verified_bot_developer\"], \"RawBulkMessageDeleteEvent\": [\"cached_messages\", \"channel_id\", \"guild_id\", \"message_ids\"], \"RawMessageDeleteEvent\": [\"cached_message\", \"channel_id\", \"guild_id\", \"message_id\"], \"RawMessageUpdateEvent\": [\"cached_message\", \"channel_id\", \"data\", \"guild_id\", \"message_id\"], \"RawReactionActionEvent\": [\"channel_id\", \"emoji\", \"event_type\", \"guild_id\", \"member\", \"message_id\", \"user_id\"], \"RawReactionClearEmojiEvent\": [\"channel_id\", \"emoji\", \"guild_id\", \"message_id\"], \"RawReactionClearEvent\": [\"channel_id\", \"guild_id\", \"message_id\"], \"Reaction\": [\"count\", \"custom_emoji\", \"emoji\", \"me\", \"message\"], \"Relationship\": [\"type\", \"user\"], \"RelationshipType\": [\"blocked\", \"friend\", \"incoming_request\", \"outgoing_request\"], \"RequestsWebhookAdapter\": [\"BASE\"], \"Role\": [\"color\", \"colour\", \"created_at\", \"guild\", \"hoist\", \"id\", \"managed\", \"members\", \"mention\", \"mentionable\", \"name\", \"permissions\", \"position\", \"tags\"], \"RoleTags\": [\"bot_id\", \"integration_id\"], \"ShardInfo\": [\"id\", \"latency\", \"shard_count\"], \"SpeakingState\": [\"none\", \"priority\", \"soundshare\", \"voice\"], \"Spotify\": [\"album\", \"album_cover_url\", \"artist\", \"artists\", \"color\", \"colour\", \"created_at\", \"duration\", \"end\", \"name\", \"party_id\", \"start\", \"title\", \"track_id\", \"type\"], \"StageChannel\": [\"bitrate\", \"category\", \"category_id\", \"changed_roles\", \"created_at\", \"guild\", \"id\", \"members\", \"mention\", \"name\", \"overwrites\", \"permissions_synced\", \"position\", \"requesting_to_speak\", \"rtc_region\", \"topic\", \"type\", \"user_limit\", \"voice_states\"], \"Status\": [\"dnd\", \"do_not_disturb\", \"idle\", \"invisible\", \"offline\", \"online\"], \"Sticker\": [\"created_at\", \"description\", \"format\", \"id\", \"image\", \"image_url\", \"name\", \"pack_id\", \"preview_image\", \"tags\"], \"StickerType\": [\"apng\", \"lottie\", \"png\"], \"StoreChannel\": [\"category\", \"category_id\", \"changed_roles\", \"created_at\", \"guild\", \"id\", \"mention\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"type\"], \"Streaming\": [\"assets\", \"created_at\", \"details\", \"game\", \"name\", \"platform\", \"twitch_name\", \"type\", \"url\"], \"SystemChannelFlags\": [\"DEFAULT_VALUE\", \"VALID_FLAGS\", \"join_notifications\", \"premium_subscriptions\", \"value\"], \"Team\": [\"icon\", \"icon_url\", \"id\", \"members\", \"name\", \"owner\", \"owner_id\"], \"TeamMember\": [\"avatar\", \"avatar_url\", \"bot\", \"color\", \"colour\", \"created_at\", \"default_avatar\", \"default_avatar_url\", \"discriminator\", \"display_name\", \"id\", \"membership_state\", \"mention\", \"name\", \"permissions\", \"public_flags\", \"system\", \"team\"], \"TeamMembershipState\": [\"accepted\", \"invited\"], \"Template\": [], \"TextChannel\": [\"category\", \"category_id\", \"changed_roles\", \"created_at\", \"guild\", \"id\", \"last_message\", \"last_message_id\", \"members\", \"mention\", \"name\", \"nsfw\", \"overwrites\", \"permissions_synced\", \"position\", \"slowmode_delay\", \"topic\", \"type\"], \"Theme\": [\"dark\", \"light\"], \"User\": [\"avatar\", \"avatar_url\", \"bot\", \"color\", \"colour\", \"created_at\", \"default_avatar\", \"default_avatar_url\", \"discriminator\", \"display_name\", \"dm_channel\", \"id\", \"mention\", \"mutual_guilds\", \"name\", \"public_flags\", \"relationship\", \"system\"], \"UserContentFilter\": [\"all_messages\", \"disabled\", \"friends\"], \"UserFlags\": [\"bug_hunter\", \"bug_hunter_level_2\", \"early_supporter\", \"has_unread_urgent_messages\", \"hypesquad\", \"hypesquad_balance\", \"hypesquad_bravery\", \"hypesquad_brilliance\", \"mfa_sms\", \"partner\", \"premium_promo_dismissed\", \"staff\", \"system\", \"team_user\", \"verified_bot\", \"verified_bot_developer\"], \"VerificationLevel\": [\"double_table_flip\", \"extreme\", \"high\", \"low\", \"medium\", \"none\", \"table_flip\", \"very_high\"], \"VersionInfo\": [\"count\", \"index\", \"major\", \"micro\", \"minor\", \"releaselevel\", \"serial\"], \"VoiceChannel\": [\"bitrate\", \"category\", \"category_id\", \"changed_roles\", \"created_at\", \"guild\", \"id\", \"members\", \"mention\", \"name\", \"overwrites\", \"permissions_synced\", \"position\", \"rtc_region\", \"type\", \"user_limit\", \"voice_states\"], \"VoiceClient\": [\"average_latency\", \"guild\", \"latency\", \"source\", \"supported_modes\", \"user\", \"warn_nacl\"], \"VoiceProtocol\": [], \"VoiceRegion\": [\"amsterdam\", \"brazil\", \"dubai\", \"eu_central\", \"eu_west\", \"europe\", \"frankfurt\", \"hongkong\", \"india\", \"japan\", \"london\", \"russia\", \"singapore\", \"south_korea\", \"southafrica\", \"sydney\", \"us_central\", \"us_east\", \"us_south\", \"us_west\", \"vip_amsterdam\", \"vip_us_east\", \"vip_us_west\"], \"VoiceState\": [\"afk\", \"channel\", \"deaf\", \"mute\", \"requested_to_speak_at\", \"self_deaf\", \"self_mute\", \"self_stream\", \"self_video\", \"session_id\", \"suppress\"], \"Webhook\": [\"avatar\", \"avatar_url\", \"channel\", \"channel_id\", \"created_at\", \"guild\", \"guild_id\", \"id\", \"name\", \"token\", \"type\", \"url\", \"user\"], \"WebhookAdapter\": [\"BASE\"], \"WebhookMessage\": [\"activity\", \"application\", \"attachments\", \"author\", \"call\", \"channel\", \"channel_mentions\", \"clean_content\", \"content\", \"created_at\", \"edited_at\", \"embeds\", \"flags\", \"guild\", \"id\", \"jump_url\", \"mention_everyone\", \"mentions\", \"nonce\", \"pinned\", \"raw_channel_mentions\", \"raw_mentions\", \"raw_role_mentions\", \"reactions\", \"reference\", \"role_mentions\", \"stickers\", \"system_content\", \"tts\", \"type\", \"webhook_id\"], \"WebhookType\": [\"channel_follower\", \"incoming\"], \"Widget\": [\"channels\", \"created_at\", \"id\", \"invite_url\", \"json_url\", \"members\", \"name\"], \"WidgetChannel\": [\"created_at\", \"id\", \"mention\", \"name\", \"position\"], \"WidgetMember\": [\"activity\", \"avatar\", \"avatar_url\", \"bot\", \"color\", \"colour\", \"connected_channel\", \"created_at\", \"deafened\", \"default_avatar\", \"default_avatar_url\", \"discriminator\", \"display_name\", \"id\", \"mention\", \"muted\", \"name\", \"nick\", \"public_flags\", \"status\", \"suppress\", \"system\"]}}"
        
    }
    
)





































def readSettings():

    global settingsJson
    global token
    global master
    global authorisedUsers
    global logFile
    global logChannel
    global streamingSettings
    global shortAutoclearTime
    global longAutoclearTime
    global maxSearchDepth
    # global allDataAttributes
    global attributeMaxLength
    global validCommands
    global serverSettings
    global defaultStatus
    global deleteMessages
    global typeEmojis
    global reactionsEnabled
    global discordClassOverridesDict
    global discordClassOverridesOverridesDict





    settingsJson = json_loads(virtualFiles["bot.json"])

    token = (os.environ["BOT_TOKEN"])
    master = settingsJson["master"]
    authorisedUsers = settingsJson["authorisedUsers"]
    logFile = settingsJson["logFile"]
    logChannel = settingsJson["logChannel"]

    streamingSettings = settingsJson["streamingSettings"]

    shortAutoclearTime = settingsJson["shortAutoclearTime"]
    longAutoclearTime = settingsJson["longAutoclearTime"]
    maxSearchDepth = settingsJson["maxDepth"]

    # allDataAttributes = settingsJson["allDataAttributes"]

    attributeMaxLength = settingsJson["attributeMaxLength"]

    validCommands = settingsJson["validCommands"]

    serverSettings = settingsJson["serverSettings"]

    defaultStatus = settingsJson["defaultStatus"]

    deleteMessages = settingsJson["deleteMessages"]

    typeEmojis = settingsJson["typeEmojis"]

    reactionsEnabled = settingsJson["reactionsEnabled"]

    discordClassOverridesDict = settingsJson["classOverrides"]

    discordClassOverridesOverridesDict = settingsJson["classOverridesOverrides"]


    # print(shortAutoclearTime)
    # print(maxSearchDepth)





def writeSettings():

    settingsJson["serverSettings"] = serverSettings




















def stripRaw(message):
    return (message.strip(" `"))







def recalculateCommands():
    global validCommands

    validCommands["preReplies"] = {

        "trollHelpEmbed": {"message": "no help for you!", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "eggEmoji": {"message": "\U0001F95A", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "handEmoji": {"message": ":wave_tone1:", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "why": {"message": "no...", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "snowflakeEmoji": {"message": ":snowflake:", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},

        "ls": {"message": "```pi@raspberrypi: ~ $ ls\nREADME.txt```", "embed": None, "deleteTime": 4, "permissions": 0},
        "cat": {"message": "```pi@raspberrypi: ~ $ cat README.txt\nwell done...```", "embed": None, "deleteTime": 4, "permissions": 0},
        "nano": {"message": "```GNU nano 3.2                       README.txt                                 \n\nwell done...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                [ Read 1 line ]                               \n^G Get Help  ^O Write Out ^W Where Is  ^K Cut Text  ^J Justify   ^C Cur Pos   \n^X Exit      ^R Read File ^\ Replace   ^U Uncut Text^T To Spell  ^_ Go To Line\n```", "embed": None, "deleteTime": 4, "permissions": 0},

        "helpEmbed": {"function": "createHelpEmbed()", "message": None, "embed": None, "deleteTime": longAutoclearTime, "permissions": 0},
        "randomNumber": {"function": "generateRandom()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},

        "upTime": {"function": "getUptime()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        # "attendanceEmbed": {"message": (format(((datetime.now()) - startTime), "code")), "embed": ((grablink(9))), "deleteTime": shortAutoclearTime, "permissions": 1},
        "attendanceEmbed": {"message": None, "embed": "timetables", "deleteTime": shortAutoclearTime, "permissions": 0},

        "getTimetables": {"message": None, "embed": "forms", "deleteTime": shortAutoclearTime, "permissions": 0},

        "prettyPrint": {"function": "prettyPrint()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "getHistory": {"function": "getHistory()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "ifEmptyCodeBlock": {"function": "generateBlock(\"Empty\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifZeroCodeBlock": {"function": "generateBlock(\"Zero\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifLongCodeBlock": {"function": "generateBlock(\"Long\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "ifGreaterCodeBlock": {"function": "generateBlock(\"Greater\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifLessCodeBlock": {"function": "generateBlock(\"Less\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifGreaterLessCodeBlock": {"function": "generateBlock(\"GreaterLess\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifTrueCodeBlock": {"function": "generateBlock(\"Truthy\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "forIteratorCodeBlock": {"function": "generateBlock(\"FIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "whileIteratorCodeBlock": {"function": "generateBlock(\"WIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "dictionaryIteratorCodeBlock": {"function": "generateBlock(\"DIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "fileCodeBlock": {"function": "generateBlock(\"Filey\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "autoClear": {"function": "removeMessages()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "generateTimetable": {"function": "getPeriod()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "removeSmirk": {"function": "removeSmirk()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "deleteCallingMessage": {"function": "deleteCallingMessage()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "writeSettings": {"function": "saveSettings()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "listAttributes": {"function": "listAttributes()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "setStatus": {"function": "setStatus()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "rebuildIndex": {"function": "rebuildIndex()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "checkForCommander": {"function": "checkForCommander()", "message": None, "embed": None, "deleteTime": 8, "permissions": 0},

        "testPing": {"function": "testPing()", "message": None, "embed": None, "deleteTime": 8, "permissions": 0},

        "acknowledgementsHelpEmbed": {"message": None, "embed": "acknowledgementsHelpEmbed", "deleteTime": shortAutoclearTime, "permissions": 1},

        "owoify": {"function": "owoify()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "startListening": {"function": "listening(True)", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "stopListening": {"function": "listening(False)", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "terminate": {"function": "terminate()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "copyUserText": {"function": "copyUserText()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},

        "revokeAllInvites": {"function": "revokeAllInvites()", "message": None, "embed": None, "deleteTime": None, "permissions": 1},

        "addListeners": {"function": "addListeners()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},

        "joinVoice": {"function": "joinVoice()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},




    }







def format(message, format, language = ""):

    message = (str(message))

    if ("code" in format):
        message = ("`" + (str(message)) + "`")
    if ("cBlock" in format):
        message = ("```" + language + "\n" + (str(message)) + "\n" + "```")
    if ("italic" in format):
        message = ("*" + (str(message)) + "*")
    if ("bold" in format):
        message = ("**" + (str(message)) + "**")
    if ("underline" in format):
        message = ("__" + (str(message)) + "__")
    if ("strikethrough" in format):
        message = ("~~" + (str(message)) + "~~")
    if ("quote" in format):
        message = ("> " + (str(message)))
        message = message.replace("\n", "\n> ")

    return message











def grablink(year):

    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds

    today = datetime.today()
    if int(today.strftime("%W")) % 2 == 0:
        week = "Week+A"
    else:
        week = "Week+B"


    if ((seconds > 31800) and (seconds <= 32280)):
        period = "RC"
    elif ((seconds > 32400) and (seconds <= 34800)):
        period = "1"
    elif ((seconds > 35100) and (seconds <= 37500)):
        period = "2"
    elif ((seconds > 38700) and (seconds <= 41100)):
        period = "3"
    elif ((seconds > 41400) and (seconds <= 43800)):
        period = "4"
    elif ((seconds > 46200) and (seconds <= 47400)):
        period = "5"
    elif ((seconds > 48900) and (seconds <= 51300)):
        period = "6"
    else:
        period = "NULL"

    if year == 8:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSdBn_QwHom86htHoZYGuG6YjXTvjL_-IJoCdoiYMVVbZMwU9g" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 9:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSc1aXXrENpHmaJ30zlmR4xWnNv6mRw4jKJSiZeUErAG9e6bdw" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 10:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSew3K82Uj9SRrtd0C1wHyC4Rn9neUmOCy1AzcCz7tRYJzFHGw" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 12:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSdqg7NnSAYiZjIafsTDwsaemF1ZRmBNi4yP5uYxEw5f0O0d6A" + "/" + "viewform" + "?" + "usp=pp_url" + "&"




    rtnval += "entry.1193583720" + "=" + today.strftime("%Y-%m-%d") + "&"
    rtnval += "entry.1166771392" + "=" + week + "&"
    rtnval += "entry.449469481" + "=" + today.strftime("%A") + "&"
    rtnval += "entry.1844771487" + "=" + today.strftime("%A") + "&"


    if week == "Week+A":
        if today.strftime("%A") == "Monday":
            rtnval += "entry.669622984" + "=" + period
        elif today.strftime("%A") == "Tuesday":
            rtnval += "entry.1898890906" + "=" + period
        elif today.strftime("%A") == "Wednesday":
            rtnval += "entry.371344035" + "=" + period
        elif today.strftime("%A") == "Thursday":
            rtnval += "entry.1449705738" + "=" + period
        elif today.strftime("%A") == "Friday":
            rtnval += "entry.524423421" + "=" + period

    elif week == "Week+B":
        if today.strftime("%A") == "Monday":
            rtnval += "entry.1662723045" + "=" + period
        elif today.strftime("%A") == "Tuesday":
            rtnval += "entry.614317995" + "=" + period
        elif today.strftime("%A") == "Wednesday":
            rtnval += "entry.855393316" + "=" + period
        elif today.strftime("%A") == "Thursday":
            rtnval += "entry.105918712" + "=" + period
        elif today.strftime("%A") == "Friday":
            rtnval += "entry.115181569" + "=" + period



    return [

        {
            "title": "Click to open",
            "url": rtnval,
            "description": "Year 9/10 only",
            "color": 0x8000C0,
        },
        {
            "name": "Attendance Form",
            "url": "",
            "icon_url": "",
        },
        {
            "text": "this is not fully automatic",
        },
        [
        ]

    ]





def generateDiscordClasses():

    global discordClassNamesDict
    global discordClassAttributesDict
    global discordClassAttributesOverridesDict
    global discordClassNameAttributesDict
    global discordClassAttributesOverridesOverridesDict

    discordModuleMembers = (inspect.getmembers(discord))
    discordModuleMembersLength = len(discordModuleMembers)
    discordClassNamesDict = {}


    repeats = 0
    while (repeats < discordModuleMembersLength):

        if ((discordModuleMembers[repeats][0])[0] == "_"):
            pass
        elif ((discordModuleMembers[repeats][0])[0] != "_"):

            if ((inspect.isclass(discordModuleMembers[repeats][1])) == True):
                discordClassNamesDict[(discordModuleMembers[repeats][1])] = (discordModuleMembers[repeats][0])
            elif ((inspect.isclass(discordModuleMembers[repeats][1])) == False):
                pass

        repeats = repeats + 1



    indexJson = json_loads(virtualFiles["index.json"])


    discordClassNameAttributesDict = indexJson["discordClassNameAttributesDict"]
    discordClassNameAttributesLength = len(discordClassNameAttributesDict)
    discordClasses = list(discordClassNamesDict.keys())

    discordClassAttributesDict = {}

    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        discordClassAttributesDict[(discordClasses[repeats])] = discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        repeats = repeats + 1




    discordClassAttributesOverridesDict = discordClassAttributesDict.copy()
    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        try:
            discordClassAttributesOverridesDict[(discordClasses[repeats])] = discordClassOverridesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        except Exception as exception:
            pass


        repeats = repeats + 1





    discordClassAttributesOverridesOverridesDict = discordClassAttributesDict.copy()
    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        try:
            discordClassAttributesOverridesOverridesDict[(discordClasses[repeats])] = discordClassOverridesOverridesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        except Exception as exception:
            pass


        repeats = repeats + 1














def regenerateClassAttributes():

    global indexJson
    global discordClassNameAttributesDict


    discordClasses = list(discordClassNamesDict.keys())


    discordClassesLength = len(discordClasses)
    discordClassNameAttributesDict = {}


    repeats = 0
    while (repeats < discordClassesLength):

        discordClassNameAttributes = (inspect.getmembers(discordClasses[repeats]))
        discordClassNameAttributesLength = (len(discordClassNameAttributes))

        discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])] = []


        repeats1 = 0
        while (repeats1 < discordClassNameAttributesLength):

            if (((discordClassNameAttributes[repeats1][0][0]) != "_") == True):

                if ((inspect.isfunction(discordClassNameAttributes[repeats1][1])) == True):
                    pass

                elif ((inspect.isfunction(discordClassNameAttributes[repeats1][1])) == False):

                    if ((inspect.ismethod(discordClassNameAttributes[repeats1][1])) == True):
                        pass

                    elif ((inspect.ismethod(discordClassNameAttributes[repeats1][1])) == False):
                        (discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])]).append(discordClassNameAttributes[repeats1][0])

            elif (((discordClassNameAttributes[repeats1][0][0]) != "_") == False):
                pass


            repeats1 = repeats1 + 1


        repeats = repeats + 1



    indexJson["discordClassNameAttributesDict"] = discordClassNameAttributesDict









def generateEmbeds():


    global generatedEmbeds

    metaInfoJson = json_loads(virtualFiles["metainfo.json"])


    prebuiltEmbedNames = list(metaInfoJson.keys())
    prebuiltEmbedNamesLength = (len(prebuiltEmbedNames))

    repeats = 0
    while (repeats < prebuiltEmbedNamesLength):

        title = (metaInfoJson[(prebuiltEmbedNames[repeats])][0])
        header = (metaInfoJson[(prebuiltEmbedNames[repeats])][1])
        footer = (metaInfoJson[(prebuiltEmbedNames[repeats])][2])
        fields = (metaInfoJson[(prebuiltEmbedNames[repeats])][3])
        fieldsLength = (len(fields))

        newEmbed = discord.Embed(**title)

        newEmbed.set_author(**header)
        newEmbed.set_footer(**footer)

        typeEmojisKeys = list(typeEmojis.keys())
        typeEmojisKeysLength = (len(typeEmojisKeys))

        repeats1 = 0
        while (repeats1 < fieldsLength):

            repeats2 = 0
            while (repeats2 < typeEmojisKeysLength):
                (fields[repeats1]["name"]) = (fields[repeats1]["name"]).replace(("$" + (typeEmojisKeys[repeats2]) + "$"), ("<" + ":" + (typeEmojisKeys[repeats2]) + ":" + (typeEmojis[(typeEmojisKeys[repeats2])]) + ">"))
                repeats2 = repeats2 + 1

            newEmbed.add_field(**(fields[repeats1]))
            repeats1 = repeats1 + 1


        generatedEmbeds[(prebuiltEmbedNames[repeats])] = newEmbed

        repeats = repeats + 1










































class MyClient(discord.Client):



    async def printOutputToLogs(self, output, message = None):

        print((repr(output)) + "\n")


        if (message == None):
            await botLogger.send(format(("Administration" + "\n\n" + output), "cBlock"))
        elif (message != None):


            if "embed" in output:
                output["embed"] = (repr(output["embed"]))

            if "reference" in output:
                output["reference"] = (repr(output["reference"]))

            if "file" in output:
                output["file"] = (repr(output["file"]))




            result = ("Replied with" + "\n\n" + (str(json_dumps(output, indent = 4))) + "\n\n\n\n" + "to" + "\n\n" + (str(message.content)) + "\n\n\n\n" + "from" + "\n\n" + (self.generateDisplayName()))
            result = (format(result, "cBlock"))


            if (len(result) < 256):
                result = result
                await botLogger.send(result)
            elif (len(result) >= 256):
                tempFile = io.BytesIO(result.encode())
                discordFile = (discord.File(tempFile, "message.txt"))
                await botLogger.send(file = discordFile)




    async def checkForCommander(self):

        if ((callingMessage.author.id) in authorisedUsers):
            return [("commanderYes", {}), "embed"]
        elif ((callingMessage.author.id) not in authorisedUsers):
            return [("commanderNo", {}), "embed"]




    async def testPing(self):
        utcTime = datetime.utcnow()
        sentTime = callingMessage.created_at
        return [("roundTripTime", {"title": "Round trip time", "description": ((format("Total:", "bolden")) + " " + (format(((str(round((((utcTime - sentTime).total_seconds()) * 1000), 3))) + " " + "ms"), "code")) + "\n" + (format("WebSocket:", "bolden")) + " " + (format(((str(round(((client.latency) * 1000), 3))) + " " + "ms"), "code")))}), "embed"]


    async def listening(self, enabled):

        global commandsEnabled
        commandsEnabled = enabled

        if (commandsEnabled == True):
            await client.change_presence(status = (discord.Status.idle), activity = (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime))))
            return [("taskCompleted", {"description": "Now listening!"}), "embed"]

        elif (commandsEnabled == False):
            await client.change_presence(status = (discord.Status.dnd), activity = (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime))))
            return [("taskCompleted", {"description": "Now sleeping!"}), "embed"]








    def generateDisplayName(self):
        return ((str(callingMessage.author.display_name)) + "#" + (str(callingMessage.author.discriminator)) + " " + "(" + (str(callingMessage.author.id)) + ")")


    async def rebuildIndex(self):

        # regenerateClassAttributes()

        # return [("taskCompleted", {"description": "index rebuilt"}), "embed"]
        return [(format("too slow for use", "code")), "message"]



    async def saveSettings(self):

        # writeSettings()

        # return [("taskCompleted", {"description": "settings saved"}), "embed"]
        return [(format("too slow for use", "code")), "message"]




    async def sendMessage(self, sendOptions, reactions = {}):

        if ((("reference" in sendOptions) == True) or (("mention_author" in sendOptions) == True)):
            sendOptions["reference"] = sendOptions["reference"]
            sendOptions["mention_author"] = sendOptions["mention_author"]
        elif ((("reference" in sendOptions) == False) and (("mention_author" in sendOptions) == False)):
            sendOptions["reference"] = (callingMessage.to_reference())
            sendOptions["mention_author"] = False



        if ((sendOptions["delete_after"]) == None):
            pass
        elif ((sendOptions["delete_after"]) != None):

            if ((str(callingMessage.guild.id)) in serverSettings):

                if ((serverSettings[(str(callingMessage.guild.id))]["deleteCalls"]) == True):
                    await callingMessage.delete(delay = 4)
                elif ((serverSettings[(str(callingMessage.guild.id))]["deleteCalls"]) == False):
                    pass

            elif ((str(callingMessage.guild.id)) not in serverSettings):
                pass


        sentMessage = await callingMessage.channel.send(**sendOptions)



        if (reactions == None):
            pass
        elif (reactions != None):
            repeats = 0
            while (repeats < (len(reactions))):
                await sentMessage.add_reaction(reactions[repeats])
                repeats = repeats + 1



        await self.printOutputToLogs(sendOptions, callingMessage)




    async def listAttributes(self):

        return [(format((json_dumps(discordClassNameAttributesDict, indent = 4)), "cBlock", "json")), "message"]



    async def setStatus(self):

        global statusScheduleOverridden
        global statusSchedulePosition



        if (virtualParameters == None):
            statusScheduleOverridden = True

        elif (virtualParameters != None):
            statusScheduleOverridden = False




        parameters = await self.getParameters()


        statuses = {

            "streaming": {
                "status": (discord.Status.idle),
                "activity": (discord.Streaming(**streamingSettings)),
            },

            "competing": {
                "status": (discord.Status.online),
                "activity": (discord.Activity(type = (discord.ActivityType.competing), name = (streamingSettings["name"]), start = (startTime)))
            },

            "online": {
                "status": (discord.Status.online),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "idle": {
                "status": (discord.Status.idle),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "dnd": {
                "status": (discord.Status.dnd),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "invisible": {
                "status": (discord.Status.invisible),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },

        }


        if (parameters == "schedule"):

            statusSchedulePosition = statusSchedulePosition



            if (statusScheduleOverridden == True):
                statusScheduleOverridden = False

            elif (statusScheduleOverridden == False):
                pass

            await self.changeStatus()


            return [("taskCompleted", {"description": ("Status set to" + " " + parameters + "!")}), "embed"]

        elif (parameters != "schedule"):


            statusSchedulePosition = -1


            if ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible))(, ?\".{0,24}\")?$", (parameters.lower())))) == True):


                if ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible)), ?\".{0,24}\"$", (parameters.lower())))) == True):
                    status = (((parameters.lower()).split(",", 1))[0])
                    activity = ((((parameters.lower()).split(",", 1))[1])[(((re.search("\".{0,24}\"", (((parameters.lower()).split(",", 1))[1]))).start()) + 1):(((re.search("\".{0,24}\"", (((parameters.lower()).split(",", 1))[1]))).end()) - 1)])

                    presence = (statuses[status])
                    
                    (presence["activity"]) = (discord.Activity(type = (discord.ActivityType.competing), name = (activity), start = (startTime)))

                    await client.change_presence(**(presence))



                    if (statusScheduleOverridden == True):
                        await self.printOutputToLogs("Changed status to" + " " + "'" + ((statuses[status]["status"]).name) + "'")
                        await self.printOutputToLogs("Changed activity to" + " " + "'" + activity + "'")

                    elif (statusScheduleOverridden == False):
                        pass




                elif ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible)), ?\".{0,24}\"$", (parameters.lower())))) == False):

                    await client.change_presence(**(statuses[(parameters.lower())]))


                    if (statusScheduleOverridden == True):
                        await self.printOutputToLogs("Changed status to" + " " + "'" + ((statuses[(parameters.lower())]["status"]).name) + "'")
                        await self.printOutputToLogs("Changed activity to" + " " + "'" + ((statuses[(parameters.lower())]["activity"]).name) + "'")

                    elif (statusScheduleOverridden == False):
                        pass




                return [("taskCompleted", {"description": ("Status set to" + " " + parameters + "!")}), "embed"]


            elif ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible))(, ?\".{0,24}\")?$", (parameters.lower())))) == False):
                # return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]
                return [("invalidParameters", {"description": ("status provided is invalid" + "\n" + "command should be in the format" + " " + (format("\\command <streaming|competing|online|idle|dnd|invisible>", "code")))}), "embed"]










    async def owoify(self):

        parameters = await self.getParameters()

        modifications = list(re.finditer(r"(([^lrw])(l{1,}|r{1,})([BCDFGHJKMNOPQSTVXYZ|bcdfghjkmnopqstvxyz]))|(([BCDFGHJKMNOPQSTVXYZ|bcdfghjkmnopqstvxyz])(l{1,}|r{1,})([^elrw\W]))", parameters))
        modificationsLength = (len(modifications))



        modificationIndex = []
        repeats = 0

        while (repeats < modificationsLength):
            modificationIndex = modificationIndex + (list(range(((((modifications[repeats]).span())[0]) + 1), ((((modifications[repeats]).span())[1]) - 1))))
            repeats = repeats + 1

        modifiedString = list(parameters)
        repeats = 0

        while (repeats < (len(modificationIndex))):
            (modifiedString[(modificationIndex[repeats])]) = "w"
            repeats = repeats + 1


        convertedString = ""
        repeats = 0
        while (repeats < (len(modifiedString))):
            convertedString = convertedString + (modifiedString[repeats])
            repeats = repeats + 1

        return [(format(convertedString, "cBlock")), "message"]



















    async def terminate(self):

        print(client.is_ws_ratelimited())

        await client.close()

        return [("taskCompleted", {}), "embed"]







    async def copyUserText(self):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\say <text>", "code")))}), "embed"]

        elif (parameters != ""):
            await callingMessage.delete(delay = 1)
            return [parameters, "message", None, [None, False]]





    async def addListeners(self):


        global pingListeningGuilds
        global pingListeningGuildsLogs
        global verificationListeningChannels
        global verificationListeningChannelsLogs
        global verificationListeningChannelsRequiredRoles
        global verificationListeningChannelsRoles
        global roleListeningChannels
        global roleListeningChannelsLogs
        global roleListeningChannelsPosition
        global roleListeningChannelsRoles
        global statusSchedule

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        print(fetchedOptions)
        # print(fetchedOptions["pings"])




        pingListeningGuilds = []
        pingListeningGuildsLogs = {}
        verificationListeningChannels = []
        verificationListeningChannelsLogs = {}
        verificationListeningChannelsRequiredRoles = {}
        verificationListeningChannelsRoles = {}
        roleListeningChannels = []
        roleListeningChannelsLogs = {}
        roleListeningChannelsPosition = {}
        roleListeningChannelsRoles = {}

        statusSchedule = (fetchedOptions["schedule"])



        repeats = 0
        while (repeats < (len(fetchedOptions["pings"]))):
            pingListeningGuilds.append(fetchedOptions["pings"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["pings"]))):
            pingListeningGuildsLogs[(fetchedOptions["pings"][repeats][0])] = fetchedOptions["pings"][repeats][1]
            repeats = repeats + 1




        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannels.append(fetchedOptions["verification"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsLogs[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][1]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsRequiredRoles[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][2]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsRoles[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][3]
            repeats = repeats + 1






        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannels.append(fetchedOptions["customRoles"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsLogs[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][1]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsPosition[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][2]
            repeats = repeats + 1

        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsRoles[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][3]
            repeats = repeats + 1





        print("\n\n\n")

        print(pingListeningGuilds, pingListeningGuildsLogs, verificationListeningChannels, verificationListeningChannelsLogs, verificationListeningChannelsRequiredRoles, verificationListeningChannelsRoles, roleListeningChannels, roleListeningChannelsLogs, roleListeningChannelsPosition, roleListeningChannelsRoles)
        print(verificationListeningChannels, verificationListeningChannelsLogs)
        print(verificationListeningChannelsRequiredRoles)
        print(verificationListeningChannelsRoles)

        print("\n\n\n")

        """

        if ((len(message.mentions)) > 0):

            if ((message.guild.id) in pingListeningGuilds):

                callingMessage = message
                messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))


        if ((len(message.role_mentions)) > 0):


            if ((message.guild.id) in pingListeningGuilds):

                callingMessage = message
                messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.role_mentions.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))



        """



        return [("taskCompleted", {"description": "Listeners updated!"}), "embed"]



    async def addRoleListener(self, channel, newRole):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["customRoles"][(roleListeningChannels.index(channel))][3]).append(newRole)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()




    async def addVerificationListener(self, verificationData):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["verification"]).append(verificationData)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()



    async def removeVerificationListener(self, verificationDataPosition):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))

        (fetchedOptions["verification"]).pop(verificationDataPosition)

        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()





    async def addMentionListener(self, mentionData):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["pings"]).append(mentionData)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()




    async def removeMentionListener(self, mentionDataPosition):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))

        (fetchedOptions["pings"]).pop(mentionDataPosition)

        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()





    async def createHelpEmbed(self):

        return [("helpMenu", {}), "embed"]


    async def joinVoice(self):


        return ["connected", "message"]


        voiceChannelToJoin = ((callingMessage.channel_mentions)[0])

        if ((voiceChannelToJoin.type) == (discord.ChannelType.voice)):

            global connectedVoiceChannels
            connectedVoiceChannels.append(await voiceChannelToJoin.connect())



        return ["connected", "message"]





    async def revokeAllInvites(self):

        guildInvites = await ((callingMessage.guild).invites())
        guildInvitesLength = (len(guildInvites))

        guildInvitesData = []

        repeats = 0
        while (repeats < guildInvitesLength):
            guildInvitesData.append(repr(self.reformatData(guildInvites[repeats])))
            await (guildInvites[repeats]).delete()
            repeats = repeats + 1


        # return [("taskCompleted", {}), "embed"]
        return [(format((json_dumps(guildInvitesData, indent = 4)), "cBlock", "json")), "message"]


















    async def deleteCallingMessage(self):

        parameters = await self.getParameters()

        print(str(callingMessage.guild.id))
        print(serverSettings)

        if ((str(callingMessage.guild.id)) in serverSettings):
            pass
        elif ((str(callingMessage.guild.id)) not in serverSettings):
            serverSettings[(str(callingMessage.guild.id))] = {}




        try:
            parameters = (self.evaluateBoolean(parameters))

        except Exception as exception:
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\dc|deletecall <enabled>", "code")))}), "embed"]


        if (parameters == True):

            serverSettings[(str(callingMessage.guild.id))]["deleteCalls"] = True
            return [("taskCompleted", {"description": "Delete calling messages set to true"}), "embed"]
            # return [(format("delete calling messages set to true", "code")), "message"]

        elif (parameters == False):

            serverSettings[(str(callingMessage.guild.id))]["deleteCalls"] = False
            return [("taskCompleted", {"description": "Delete calling messages set to false"}), "embed"]
            # return [(format("delete calling messages set to false", "code")), "message"]




    async def removeSmirk(self):

        parameters = await self.getParameters()


        smirkEmoji = "\U0001F60F"


        try:
            smirkUser = ((parameters.split(" ", 1))[0])
            limit = ((parameters.split(" ", 1))[1])

        except Exception as exception:
            return [("unspecifiedParameters", {"description": ("parameter missing" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]

        await self.createProgress(0)

        try:
            limit = (int(limit))

            if ((limit >= 0) and (limit <= 128)):
                pass
            elif (limit < 0):
                await self.createProgress(100)
                return [("invalidParameters", {"description": ("search limit is too low" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]
            elif (limit > 128):
                await self.createProgress(100)
                return [("invalidParameters", {"description": ("search limit is too high" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]


        except Exception as exception:
            await self.createProgress(100)
            return [("invalidParameters", {"description": ("search limit is not an integer" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]

        try:
            smirkUser = await client.fetch_user(smirkUser)

        except Exception as exception:
            await self.createProgress(100)
            return [("invalidParameters", {"description": ("user id provided is invalid" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]


        await self.createProgress(20)

        his = await ((callingMessage.channel.history(limit = limit)).flatten())

        repeats = 0
        while (repeats < (len(his))):

            reactionsLength = (len((his[repeats]).reactions))

            repeats1 = 0
            while (repeats1 < reactionsLength):

                # print(((his[repeats]).reactions)[repeats1])

                if (((((his[repeats]).reactions)[repeats1]).emoji) == smirkEmoji):
                    await (his[repeats]).remove_reaction(smirkEmoji, smirkUser)
                elif (((((his[repeats]).reactions)[repeats1]).emoji) != smirkEmoji):
                    pass

                repeats1 = repeats1 + 1



            if ((repeats % (round((len(his)) / 3))) == 0):

                if (repeats == 0):
                    pass
                elif (repeats != 0):
                    await self.createProgress(((repeats / (round((len(his)) / 3))) * 20) + 20)

            elif ((repeats % (round((len(his)) / 3))) != 0):
                pass



            repeats = repeats + 1


        await self.createProgress(100)

        return [("taskCompleted", {"description": "Smirks removed!"}), "embed"]













    async def changeStatus(self):


        global statusSchedulePosition
        global virtualParameters

        print("Changing status")


        timeOffset = 39600
        secondsElapsed = ((((datetime.now()).timestamp()) + timeOffset) % 86400)


        
        if (statusScheduleOverridden == True):
            pass

        elif (statusScheduleOverridden == False):

            statusScheduleLength = (len(statusSchedule))

            repeats = 0
            while (repeats < statusScheduleLength):

                if ((secondsElapsed >= (((statusSchedule[repeats])[0])[0])) and (secondsElapsed < (((statusSchedule[repeats])[0])[1]))):
                    
                    if (repeats == statusSchedulePosition):
                        pass

                    elif (repeats != statusSchedulePosition):

                        statusSchedulePosition = repeats
                        virtualParameters = ((statusSchedule[statusSchedulePosition])[1])
                        await self.setStatus()
                        break

                elif ((secondsElapsed < (((statusSchedule[repeats])[0])[0])) or (secondsElapsed >= (((statusSchedule[repeats])[0])[1]))):
                    repeats = repeats + 1
                    


















    async def getPeriod(self):

        now = datetime.now()
        midnight = now.replace(hour = 0, minute = 0, second = 0, microsecond=0)
        seconds = (now - midnight).seconds

        if int(now.strftime("%W")) % 2 == 0:
            week = "Week A"
        else:
            week = "Week B"


        day = (now.strftime("%A"))


        if (day == "Monday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 33600)):
                period = "Roll Call"
                startTime = 31800
                endTime = 33600

            elif ((seconds > 33600) and (seconds <= 36600)):
                period = "Period 1"
                startTime = 33600
                endTime = 36600

            elif ((seconds > 36600) and (seconds <= 39600)):
                period = "Period 2"
                startTime = 36600
                endTime = 39600

            elif ((seconds > 39600) and (seconds <= 40800)):
                period = "Recess"
                startTime = 39600
                endTime = 40800

            elif ((seconds > 40800) and (seconds <= 43740)):
                period = "Period 3"
                startTime = 40800
                endTime = 43740

            elif ((seconds > 43740) and (seconds <= 46680)):
                period = "Period 4"
                startTime = 43740
                endTime = 46680

            elif ((seconds > 46680) and (seconds <= 49020)):
                period = "Lunch"
                startTime = 46680
                endTime = 49020

            elif ((seconds > 49020) and (seconds <= 51960)):
                period = "Period 5"
                startTime = 49020
                endTime = 51960

            elif ((seconds > 51960) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51960
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400








        elif (day == "Tuesday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35100)):
                period = "Period 1"
                startTime = 32280
                endTime = 35100

            elif ((seconds > 35100) and (seconds <= 37920)):
                period = "Period 2"
                startTime = 35100
                endTime = 37920

            elif ((seconds > 37920) and (seconds <= 39000)):
                period = "Recess"
                startTime = 37920
                endTime = 39000

            elif ((seconds > 39000) and (seconds <= 41820)):
                period = "Period 3"
                startTime = 39000
                endTime = 41820

            elif ((seconds > 41820) and (seconds <= 44640)):
                period = "Period 4"
                startTime = 41820
                endTime = 44640

            elif ((seconds > 44640) and (seconds <= 45720)):
                period = "Lunch"
                startTime = 44640
                endTime = 45720

            elif ((seconds > 45720) and (seconds <= 48540)):
                period = "Period 5"
                startTime = 45720
                endTime = 48540

            elif ((seconds > 48540) and (seconds <= 51360)):
                period = "Period 6"
                startTime = 48540
                endTime = 51360

            elif ((seconds > 51360) and (seconds <= 86400)):
                period = "After School"
                startTime = 51360
                endTime = 86400








        elif (day == "Wednesday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35640)):
                period = "Period 1"
                startTime = 32280
                endTime = 35640

            elif ((seconds > 35640) and (seconds <= 39000)):
                period = "Period 2"
                startTime = 35640
                endTime = 39000

            elif ((seconds > 39000) and (seconds <= 40200)):
                period = "Recess"
                startTime = 39000
                endTime = 40200

            elif ((seconds > 40200) and (seconds <= 43560)):
                period = "Period 3"
                startTime = 40200
                endTime = 43560

            elif ((seconds > 43560) and (seconds <= 46800)):
                period = "Period 4"
                startTime = 43560
                endTime = 46800

            elif ((seconds > 46800) and (seconds <= 52200)):
                period = "Lunch"
                startTime = 46800
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 52200)):
                period = "Period 5"
                startTime = 52200
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 52200)):
                period = "Period 6"
                startTime = 52200
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 86400)):
                period = "After School"
                startTime = 52200
                endTime = 86400








        elif (day == "Thursday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35280)):
                period = "Period 1"
                startTime = 32280
                endTime = 35280

            elif ((seconds > 35280) and (seconds <= 38280)):
                period = "Period 2"
                startTime = 35280
                endTime = 38280

            elif ((seconds > 38280) and (seconds <= 39480)):
                period = "Recess"
                startTime = 38280
                endTime = 39480

            elif ((seconds > 39480) and (seconds <= 42480)):
                period = "Period 3"
                startTime = 39480
                endTime = 42480

            elif ((seconds > 42480) and (seconds <= 45480)):
                period = "Period 4"
                startTime = 42480
                endTime = 45480

            elif ((seconds > 45480) and (seconds <= 48900)):
                period = "Lunch"
                startTime = 45480
                endTime = 48900

            elif ((seconds > 48900) and (seconds <= 51900)):
                period = "Period 5"
                startTime = 48900
                endTime = 51900

            elif ((seconds > 51900) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51900
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400








        elif (day == "Friday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35460)):
                period = "Period 1"
                startTime = 32280
                endTime = 35460

            elif ((seconds > 35460) and (seconds <= 38640)):
                period = "Period 2"
                startTime = 35460
                endTime = 38640

            elif ((seconds > 38640) and (seconds <= 39840)):
                period = "Recess"
                startTime = 38640
                endTime = 39840

            elif ((seconds > 39840) and (seconds <= 43020)):
                period = "Period 3"
                startTime = 39840
                endTime = 43020

            elif ((seconds > 43020) and (seconds <= 46200)):
                period = "Period 4"
                startTime = 43020
                endTime = 46200

            elif ((seconds > 46200) and (seconds <= 48540)):
                period = "Lunch"
                startTime = 46200
                endTime = 48540

            elif ((seconds > 48540) and (seconds <= 51720)):
                period = "Period 5"
                startTime = 48540
                endTime = 51720

            elif ((seconds > 51720) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51720
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400





        elif ((day == "Saturday") or (day == "Sunday")):


            if ((seconds > 00000) and (seconds <= 31800)):
                period = "Before School"
                startTime = 00000
                endTime = 31800
            elif ((seconds > 31800) and (seconds <= 32400)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32400
            elif ((seconds > 32400) and (seconds <= 34800)):
                period = "Period 1"
                startTime = 32400
                endTime = 34800
            elif ((seconds > 34800) and (seconds <= 35100)):
                period = "Break 1-2"
                startTime = 34800
                endTime = 35100
            elif ((seconds > 35100) and (seconds <= 37500)):
                period = "Period 2"
                startTime = 35100
                endTime = 37500
            elif ((seconds > 37500) and (seconds <= 38700)):
                period = "Recess"
                startTime = 37500
                endTime = 38700
            elif ((seconds > 38700) and (seconds <= 41100)):
                period = "Period 3"
                startTime = 38700
                endTime = 41100
            elif ((seconds > 41100) and (seconds <= 41400)):
                period = "Break 3-4"
                startTime = 41100
                endTime = 41400
            elif ((seconds > 41400) and (seconds <= 43800)):
                period = "Period 4"
                startTime = 41400
                endTime = 43800
            elif ((seconds > 43800) and (seconds <= 46200)):
                period = "Lunch"
                startTime = 43800
                endTime = 46200
            elif ((seconds > 46200) and (seconds <= 48600)):
                period = "Period 5"
                startTime = 46200
                endTime = 48600
            elif ((seconds > 48600) and (seconds <= 48900)):
                period = "Break 5-6"
                startTime = 48600
                endTime = 48900
            elif ((seconds > 48900) and (seconds <= 51300)):
                period = "Period 6"
                startTime = 48900
                endTime = 51300
            elif ((seconds > 51300) and (seconds <= 86400)):
                period = "After School"
                startTime = 51300
                endTime = 86400
            else:
                period = "NULL"




        return [("timetable", {"title": "Current Period", "description": ("<@&877323402329866240>" + " " + "It is" + " " + ((datetime.today()).strftime("%A")) + ", " + week + ", " + period + "\n" + "Starting" + " " + ("<" + "t" + ":" + (str((int(midnight.timestamp())) + startTime)) + ":" + "R" + ">") + " and " + "Ending" + " " + ("<" + "t" + ":" + (str((int(midnight.timestamp())) + endTime)) + ":" + "R" + ">"))}), "embed"]




    async def removeMessages(self):

        parameters = await self.getParameters()

        try:
            limit = (int(parameters))

            if ((limit >= 0) and (limit <= 128)):
                pass
            elif (limit < 0):
                return [("invalidParameters", {"description": ("search limit is too low" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]
            elif (limit > 128):
                return [("invalidParameters", {"description": ("search limit is too high" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]

        except Exception as exception:
            return [("invalidParameters", {"description": ("search limit is not an integer" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]


        his = await ((callingMessage.channel.history(limit = limit)).flatten())
        hisLen = (len(his))

        repeats = 0
        while (repeats < hisLen):

            if (((his[repeats]).author.id) == (self.user.id)):
                await (his[repeats]).delete()

            repeats = repeats + 1

        return [("taskCompleted", {"description": "Messages cleared!"}), "embed"]











    async def getParameters(self):

        global virtualParameters

        if (virtualParameters == None):

            try:
                parameters = (str((((callingMessage.content)[1:]).split(" ", 1))[1]))
            except Exception as exception:
                parameters = ""

        elif (virtualParameters != None):
            parameters = (str(virtualParameters))
            virtualParameters = None

        return parameters





    def createEmbed(self, embedName, modifications = {}):

        newEmbed = generatedEmbeds[embedName]
        newEmbed.set_footer(text = ("Requested by" + " " + (self.generateDisplayName())), icon_url = (callingMessage.author.avatar_url))

        if ("title" in modifications):
            newEmbed.title = (modifications["title"])
        if ("description" in modifications):
            newEmbed.description = (modifications["description"])
        if ("author" in modifications):
            newEmbed.author = (modifications["author"])

        return newEmbed



    async def getUptime(self):
        return [("uptime", {"title": "Time since start", "description": ((format("Time:", "bolden")) + " " + (format(((datetime.now()) - startTime), "code")))}), "embed"]



    async def generateRandom(self):


        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

        elif (parameters != ""):

            try:
                startValue = ((parameters.split(" ", 1))[0])
                endValue = ((parameters.split(" ", 1))[1])

                try:
                    startValue = (int(startValue))
                    endValue = (int(endValue))

                    if (startValue <= endValue):
                        startValue = startValue
                        endValue = endValue
                    elif (startValue > endValue):
                        tempValue = startValue
                        startValue = endValue
                        endValue = tempValue

                    if ((startValue >= -18446744073709551615) and (startValue <= 18446744073709551615)):
                        pass
                    elif ((startValue < -18446744073709551615) or (startValue > 18446744073709551615)):
                        return [("invalidParameters", {"description": ("start value is out of range" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

                    if ((endValue >= -18446744073709551615) and (endValue <= 18446744073709551615)):
                        pass
                    elif ((endValue < -18446744073709551615) or (endValue > 18446744073709551615)):
                        return [("invalidParameters", {"description": ("start value is out of range" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

                    return [("randomNumber", {"title": "Random number Generator", "description": ((format("Result:", "bolden")) + " " + (format(("    " + (str(random_randint(startValue, endValue))) + "    "), "code")))}), "embed"]

                except Exception as exception:
                    return [("invalidParameters", {"description": ("values provided are not integers" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

            except Exception as exception:
                return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]





    async def generateBlock(self, type):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]

        elif (parameters != ""):

            comment = ""

            if ((parameters.isidentifier()) == True):
                comment = comment
            elif ((parameters.isidentifier()) == False):
                comment = comment + "# variable name is not valid\n"

            if ((len(parameters)) <= 1024):
                comment = comment
            elif ((len(parameters)) > 1024):
                return [("invalidParameters", {"description": ("variable name is too long" + "\n" + "command should be in the format" + " " + (format("\\command <variable> <size>", "code")))}), "embed"]

            if (type == "Zero"):
                return [(format((comment + "\nif (" + parameters + " == 0):\n    print(" + parameters + ")\nelif (" + parameters + " != 0):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "Empty"):
                return [(format((comment + "\nif (" + parameters + " == \"\"):\n    print(" + parameters + ")\nelif (" + parameters + " != \"\"):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "Long"):
                return [(format((comment + "\nif ((len(" + parameters + ")) == 0):\n    print(" + parameters + ")\nelif ((len(" + parameters + ")) != 0):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]


            elif ((type == "Greater") or (type == "Less") or (type == "GreaterLess")):

                comment = ""

                try:
                    variable = ((parameters.split(" ", 1))[0])
                    size = ((parameters.split(" ", 1))[1])
                except Exception as exception:
                    return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <variable> <size>", "code")))}), "embed"]

                if ((variable.isidentifier()) == True):
                    comment = comment
                elif ((variable.isidentifier()) == False):
                    comment = "# variable name is not valid\n"

                if ((size.isdigit()) == True):
                    comment = comment
                elif ((size.isdigit()) == False):
                    comment = comment + "# int provided is not valid\n"

                if (type == "Greater"):
                    return [(format((comment + "\nif (" + variable + " > " + size + "):\n    print(" + variable + ")\nelif (" + variable + " <= " + size + "):\n    pass"), "cBlock", "python")), "message"]
                elif (type == "Less"):
                    return [(format((comment + "\nif (" + variable + " < " + size + "):\n    print(" + variable + ")\nelif (" + variable + " >= " + size + "):\n    pass"), "cBlock", "python")), "message"]
                elif (type == "GreaterLess"):

                    comment = ""

                    try:
                        minsize = ((size.split(" ", 1))[0])
                        maxsize = ((size.split(" ", 1))[1])

                        try:
                            (int(minsize))
                            (int(maxsize))

                            if ((int(minsize)) < (int(maxsize))):
                                comment = comment
                            elif ((int(minsize)) >= (int(maxsize))):
                                comment = comment + "# arguments are not valid in this context\n"

                            if ((variable.isidentifier()) == True):
                                comment = comment
                            elif ((variable.isidentifier()) == False):
                                comment = "# variable name is not valid\n"

                        except Exception as exception:
                            comment = comment + "# arguments are not valid in this context\n"


                    except Exception as exception:
                        return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <variable> <minsize> <maxsize>", "code")))}), "embed"]

                    return [(format((comment + "\nif ((" + variable + " > " + minsize + ") and (" + variable + " <= " + maxsize + ")):\n    print(" + variable + ")\nelif ((" + variable + " <= " + minsize + ") or (" + variable + " > " + maxsize + ")):\n    pass"), "cBlock", "python")), "message"]

            elif (type == "Truthy"):
                return [(format((comment + "\nif (" + parameters + " == True):\n    print(" + parameters + ")\nelif (" + parameters + " == False):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "FIterator"):
                return [(format((comment + "\nfor (i in " + parameters + "):\n    print(i)"), "cBlock", "python")), "message"]
            elif (type == "WIterator"):
                return [(format((comment + "\n" + parameters + "Length = (len(" + parameters + "))\n\nrepeats = 0\nwhile (repeats < " + parameters + "Length):\n    print(" + parameters + "[repeats])\n    repeats = repeats + 1"), "cBlock", "python")), "message"]
            elif (type == "DIterator"):
                return [(format((comment + "\n" + parameters + "Keys = list(" + parameters + ".keys())\n" + parameters + "KeysLength = (len(" + parameters + "Keys))\nrepeats = 0\nwhile (repeats < " + parameters + "KeysLength):\n    print(" + parameters + "[(" + parameters + "Keys[repeats])])\n    repeats = repeats + 1"), "cBlock", "python")), "message"]
            elif (type == "Filey"):
                return [(format((comment + "\n" + "# import json\n" + parameters + "File = open(r\"C:\\Users\", \"r\")\n" + parameters + "Text = " + parameters + "File.read()\n" + parameters + "Json = json.loads(" + parameters + "Text)\n" + parameters + "File.close()"), "cBlock", "python")), "message"]




    async def readIcal(self):

        print(callingMessage)

        if ((((((callingMessage.attachments)[0]).filename)[-3:]) == "ics") and (((((callingMessage.attachments)[0]).filename)[0:12]) == "my_timetable") and ((((callingMessage.attachments)[0]).size) < 102400)):
            print(((callingMessage.attachments)[0]))
            rawIcal = await (((callingMessage.attachments)[0]).read())
            print(rawIcal)

        return [("unused"), "message"]






    async def prettyPrint(self):

        parameters = await self.getParameters()



        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]

        elif (parameters != ""):

            try:
                jsonDictionary = (json_loads(str(parameters)))
                prettyJsonDictionary = json_dumps(jsonDictionary, indent = 4)
                return [(format(prettyJsonDictionary, "cBlock", "json")), "message"]
            except Exception as exception:
                return [(format(("Invalid JSON" + ", " + "(" + (str(exception)) + ")"), "code")), "message"]






    def reformatIterable(self, data, maxDepth = 2, depth = 1):

        if (depth <= maxDepth):


            if ((type(data)) == tuple):

                data = (list(data))

                dataLength = (len(data))
                repeats1 = 0
                while (repeats1 < dataLength):
                    data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1

                data = (tuple(data))

            elif ((type(data)) == dict):

                dataKeys = list(data.keys())

                dataKeysLength = (len(dataKeys))
                repeats1 = 0
                while (repeats1 < dataKeysLength):
                    data[dataKeys] = data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1

            elif ((type(data)) == list):

                dataLength = (len(data))
                repeats1 = 0
                while (repeats1 < dataLength):
                    data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1


            return (data)


        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == tuple) or ((type(data)) == dict) or ((type(data)) == list)):
                    return (data)
                elif (((type(data)) != tuple) and ((type(data)) != dict) and ((type(data)) != list)):
                    return (repr(data))








    def reformatJSON(self, jsonToFormat):

        if ((type(jsonToFormat)) == dict):

            jsonToFormatKeys = list(jsonToFormat.keys())
            jsonToFormatKeysLength = (len(jsonToFormatKeys))
            
            repeats = 0
            while (repeats < jsonToFormatKeysLength):

                if ((type(jsonToFormat[(jsonToFormatKeys[repeats])])) == dict):
                    
                    if ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) == 0):
                        del(jsonToFormat[(jsonToFormatKeys[repeats])])
                    elif ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) == 1):
                        jsonToFormat[((jsonToFormatKeys[repeats]) + "." + ((list((jsonToFormat[(jsonToFormatKeys[repeats])]).keys()))[0]))] = ((jsonToFormat[(jsonToFormatKeys[repeats])])[((list((jsonToFormat[(jsonToFormatKeys[repeats])]).keys()))[0])])
                        del(jsonToFormat[(jsonToFormatKeys[repeats])])
                    elif (((len(jsonToFormat[(jsonToFormatKeys[repeats])])) != 0) and ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) != 1)):
                        (jsonToFormat[(jsonToFormatKeys[repeats])]) = self.reformatJSON(jsonToFormat[(jsonToFormatKeys[repeats])])
                        
                elif ((type(jsonToFormat[(jsonToFormatKeys[repeats])])) == list):
                    (jsonToFormat[(jsonToFormatKeys[repeats])]) = self.reformatJSON(jsonToFormat[(jsonToFormatKeys[repeats])])

                repeats = repeats + 1



            return jsonToFormat


        elif ((type(jsonToFormat)) == list):

            jsonToFormatLength = (len(jsonToFormat))

            repeats = 0
            while (repeats < jsonToFormatLength):

                if ((type(jsonToFormat[repeats])) == dict):
                    jsonToFormat[repeats] = self.reformatJSON(jsonToFormat[repeats])
                elif ((type(jsonToFormat[repeats])) == list):
                    jsonToFormat[repeats] = self.reformatJSON(jsonToFormat[repeats])

                    
                repeats = repeats + 1



            return jsonToFormat











    def reformatCategory(self, data, maxDepth = 1, depth = 1):

        if (depth <= maxDepth):



            if (depth < maxDepth):
                wantedAttributes = (discordClassAttributesOverridesDict[(type(data))])
            elif (depth >= maxDepth):
                wantedAttributes = (discordClassAttributesOverridesOverridesDict[(type(data))])


            wantedAttributesLength = (len(wantedAttributes))
            knownAttributes = {}

            repeats = 0
            while (repeats < wantedAttributesLength):

                try:

                    newAttribute = (eval("data" + "." + (wantedAttributes[repeats])))


                    if ((type(newAttribute)) in discordClassNamesDict):

                        if ((isinstance(newAttribute, (discord.Asset))) == True):
                            newAttribute = (str(newAttribute))
                        elif ((isinstance(newAttribute, (discord.Asset))) == False):
                            newAttribute = self.reformatCategory(newAttribute, maxDepth, (depth + 1))

                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):

                        newAttribute = (list(newAttribute))

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1)))
                            repeats1 = repeats1 + 1

                        newAttribute = (tuple(newAttribute))

                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):

                        newAttributeKeys = list(newAttribute.keys())

                        newAttributeKeysLength = (len(newAttributeKeys))
                        repeats1 = 0
                        while (repeats1 < newAttributeKeysLength):
                            newAttribute[newAttributeKeys] = (repr(newAttribute[newAttributeKeys]))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == list):

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1)))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:

                        try:
                            newAttribute = [(newAttribute.name), (newAttribute.value)]

                        except Exception as exception:
                            newAttribute = (repr(newAttribute))


                    knownAttributes[(wantedAttributes[repeats])] = newAttribute

                except Exception as exception:
                    knownAttributes[(wantedAttributes[repeats])] = None

                repeats = repeats + 1

            return knownAttributes









        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == str) or ((type(data)) == int) or ((type(data)) == float) or ((type(data)) == tuple) or ((type(data)) == bool) or ((type(data)) == dict) or ((type(data)) == list) or ((type(data)) == datetime)):
                    return (data)
                elif (((type(data)) != str) and ((type(data)) != int) and ((type(data)) != float) and ((type(data)) != tuple) and ((type(data)) != bool) and ((type(data)) != dict) and ((type(data)) != list) and ((type(data)) != datetime)):
                    return (repr(data))

















    def reformatMessage(self, data, maxDepth = 1, depth = 1):

        if (depth <= maxDepth):

            wantedAttributes = [
                "channel.name",
                "author.display_name",
                "created_at",
                "content",
            ]


            wantedAttributesLength = (len(wantedAttributes))
            knownAttributes = {}

            repeats = 0
            while (repeats < wantedAttributesLength):

                try:

                    newAttribute = (eval("data" + "." + (wantedAttributes[repeats])))


                    if ((type(newAttribute)) in discordClassNamesDict):
                        newAttribute = self.reformatCategory(newAttribute, maxDepth, (depth + 1))
                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):

                        newAttributeKeys = list(newAttribute.keys())

                        newAttributeKeysLength = (len(newAttributeKeys))
                        repeats1 = 0
                        while (repeats1 < newAttributeKeysLength):
                            newAttribute[newAttributeKeys] = (repr(newAttribute[newAttributeKeys]))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == list):

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (repr(self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1))))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:
                        newAttribute = (repr(newAttribute))

                    knownAttributes[(wantedAttributes[repeats])] = newAttribute

                except Exception as exception:
                    knownAttributes[(wantedAttributes[repeats])] = None

                repeats = repeats + 1


            return knownAttributes









        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == str) or ((type(data)) == int) or ((type(data)) == float) or ((type(data)) == tuple) or ((type(data)) == bool) or ((type(data)) == dict) or ((type(data)) == list) or ((type(data)) == datetime)):
                    return (data)
                elif (((type(data)) != str) and ((type(data)) != int) and ((type(data)) != float) and ((type(data)) != tuple) and ((type(data)) != bool) and ((type(data)) != dict) and ((type(data)) != list) and ((type(data)) != datetime)):
                    return (repr(data))




















    def reformatData(self, data, maxDepth = 3, depth = 1):

        if (depth <= maxDepth):

            returnData = {}

            dataAttributes = discordClassAttributesDict[(type(data))]
            dataLength = (len(dataAttributes))

            repeats = 0
            while (repeats < (dataLength - 1)):

                try:

                    newAttribute = (getattr(data, (dataAttributes[repeats])))

                    if ((type(newAttribute)) in discordClassNamesDict):
                        newAttribute = self.reformatData(newAttribute, maxDepth, (depth + 1))
                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):
                        newAttribute = (repr(newAttribute))
                    elif ((type(newAttribute)) == list):
                        newAttribute = (repr(newAttribute))
                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:
                        newAttribute = (repr(newAttribute))


                    if (len(newAttribute) < attributeMaxLength):
                        newAttribute = newAttribute
                    elif (len(newAttribute) >= attributeMaxLength):
                        newAttribute = ("<" + "Warning" + ":" + " " + "Attribute is longer than" + " " + (str(attributeMaxLength)) + " " + "characters" + ">")

                    returnData[(dataAttributes[repeats])] = newAttribute

                except Exception as exception:

                    returnData[(dataAttributes[repeats])] = (None)




                repeats = repeats + 1

            return [(returnData), "message"]

        elif (depth > maxDepth):
            return [(repr(data)), "message"]






    def evaluateBoolean(self, booleanString):
        booleanYes = ["true", "1", "=", "+", "on", "yes"]
        booleanNo = ["false", "0", "-", "off", "no"]

        if ((booleanString.lower()) in booleanYes):
            return True
        elif ((booleanString.lower()) in booleanNo):
            return False
        else:
            raise Exception("ERROR")






    def evaluatePositive(self, positiveInt):

        if (positiveInt < 1):
            raise Exception("ERROR")
        elif (positiveInt >= 1):
            pass



    async def createProgress(self, percentage):

        global progressMessage
        global progressMessagePercentage

        if (percentage == progressMessagePercentage):
            pass
        elif (percentage != progressMessagePercentage):

            if (percentage < 100):

                progressMessagePercentage = percentage

                width = 20
                progressCharacters = ["\u2593", "\u2591"]

                progress = (percentage / 100)

                progressDisplay = ""
                progressDisplay = progressDisplay.ljust((round(progress * width)), (progressCharacters[0]))
                progressDisplay = progressDisplay.ljust((round(width)), (progressCharacters[1]))

                if (progressMessage == None):

                    progressMessage = await callingMessage.channel.send(content = ("processing" + ": " + progressDisplay + " " + (str(percentage)) + "%"), embed = None)
                    await callingMessage.channel.trigger_typing()

                elif (progressMessage != None):

                    await progressMessage.edit(content = ("processing" + ": " + progressDisplay + " " + (str(percentage)) + "%"), embed = None)

            elif (percentage >= 100):

                if (progressMessage == None):
                    pass
                elif (progressMessage != None):

                    await progressMessage.delete()

                    progressMessage = None










    async def getHistory(self):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <message|server|channel|category> <condensed> <searchlimit> <depth>", "code")))}), "embed"]

        elif (parameters != ""):

            await self.createProgress(0)

            try:
                type = ((parameters.split(" ", 3))[0])
                condensed = ((parameters.split(" ", 3))[1])
                collapsed = ((parameters.split(" ", 3))[2])
                options = ((parameters.split(" ", 3))[3])

                messageLimit = ((options.split(" ", 1))[0])
                maximumDepth = ((options.split(" ", 1))[1])



                condensed = (self.evaluateBoolean(condensed))
                collapsed = (self.evaluateBoolean(collapsed))

                messageLimit = (int(messageLimit))
                maximumDepth = (int(maximumDepth))

                self.evaluatePositive(messageLimit)
                self.evaluatePositive(maximumDepth)


            except Exception as exception:
                return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]


            attribs = []
            dataToSend = {}

            await self.createProgress(10)

            if (condensed == True):






                if (type == "message"):

                    if (((messageLimit * (8 ** maximumDepth)) >= 0) and ((messageLimit * (8 ** maximumDepth)) <= 262144)):
                        pass
                    elif ((messageLimit * (8 ** maximumDepth)) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((messageLimit * (8 ** maximumDepth)) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]



                    messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())

                    await self.createProgress(40)

                    messageHistoryLength = (len(messageHistory))

                    repeats = 0
                    while (repeats < messageHistoryLength):

                        attribs.append(self.reformatCategory((messageHistory[repeats]), maximumDepth))

                        repeats = repeats + 1


                    await self.createProgress(60)


                    dataToSend["common"] = {}
                    dataToSend["common"]["guild.id"] = ((messageHistory[0]).guild.id)
                    dataToSend["common"]["channel.category.id"] = ((messageHistory[0]).channel.category.id)
                    dataToSend["common"]["channel.id"] = ((messageHistory[0]).channel.id)


                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["messages"] = attribs


                elif (type == "server"):

                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    await self.createProgress(40)

                    attribs.append(self.reformatCategory(((messageHistory[0]).guild), maximumDepth))

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs

                    dataToSend["server"] = attribs





                elif (type == "channel"):

                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]

                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())
                    channelsLength = (len((messageHistory[0]).guild.channels))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < channelsLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.channels[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["channels"] = attribs


                elif (type == "role"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    rolesLength = (len((messageHistory[0]).guild.roles))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < rolesLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.roles[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)




                    dataToSend["common"] = {}
                    dataToSend["common"]["guild.id"] = ((messageHistory[0]).guild.id)


                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["roles"] = attribs



                elif (type == "member"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    membersLength = (len((messageHistory[0]).guild.members))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < membersLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.members[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["members"] = attribs




                elif (type == "emoji"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    emojisLength = (len((messageHistory[0]).guild.emojis))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < emojisLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.emojis[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs

                    
                    dataToSend["emojis"] = attribs




                elif ((type != "message") and (type != "server") and (type != "channel") and (type != "role") and (type != "member") and (type != "emoji")):
                    await self.createProgress(100)
                    return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]











            elif (condensed == False):








                if (type == "message"):

                    if (((messageLimit * (8 ** maximumDepth)) >= 0) and ((messageLimit * (8 ** maximumDepth)) <= 256)):
                        pass
                    elif ((messageLimit * (8 ** maximumDepth)) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((messageLimit * (8 ** maximumDepth)) > 256):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())

                    await self.createProgress(40)

                    messageHistoryLength = (len(messageHistory))

                    repeats = 0
                    while (repeats < messageHistoryLength):

                        attribs.append(self.reformatData((messageHistory[repeats]), maximumDepth))
                        print(messageHistory[repeats])
                        # return (repr(attribs))

                        repeats = repeats + 1


                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["messages"] = attribs






                elif (type == "server"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "channel"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "role"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]


                elif (type == "member"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "emoji"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]


                elif ((type != "message") and (type != "server") and (type != "channel") and (type != "role") and (type != "member") and (type != "emoji")):
                    await self.createProgress(100)
                    return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]





            await self.createProgress(80)

            await self.createProgress(100)



            # print(dataToSend)


            dataToSend["metadata"] = {}
            dataToSend["metadata"]["message"] = (callingMessage.jump_url)
            dataToSend["metadata"]["caller"] = (callingMessage.author.id)
            dataToSend["metadata"]["guild"] = (callingMessage.guild.id)
            dataToSend["metadata"]["date"] = ((callingMessage.created_at).isoformat())
            dataToSend["metadata"]["parameters"] = {}
            dataToSend["metadata"]["parameters"]["type"] = type
            dataToSend["metadata"]["parameters"]["condensed"] = condensed
            dataToSend["metadata"]["parameters"]["messageLimit"] = messageLimit
            dataToSend["metadata"]["parameters"]["maximumDepth"] = maximumDepth




            return [(format((json_dumps(dataToSend, indent = 2)), "cBlock", "json")), "message"]








    async def createMessage(self, originalMessage, function = None, message = "\u200B", embed = None, deleteTime = None, permissions = 0):

        global callingMessage
        callingMessage = originalMessage

        passedPerms = True
        file = None

        if ((permissions & 1) == 1):

            if ((originalMessage.author.id) in authorisedUsers):
                passedPerms = passedPerms & True
            elif ((originalMessage.author.id) not in authorisedUsers):
                passedPerms = passedPerms & False
                await self.sendMessage({"content": None, "embed": (self.createEmbed("unauthorisedUser", {"description": (format(("You have not been authorised to use the command" + " " + "[" + (((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) + "]" + "!"), "code"))})), "delete_after": 8, "allowed_mentions": None})

        elif ((permissions & 1) != 1):
            passedPerms = passedPerms & True


        if ((permissions & 2) == 2):
            passedPerms = passedPerms & True
        elif ((permissions & 2) != 2):

            if (commandsEnabled == True):
                passedPerms = passedPerms & True
            elif (commandsEnabled == False):
                passedPerms = passedPerms & False
                await self.sendMessage({"content": None, "embed": (self.createEmbed("commandDisabled", {"description": (format(("The command" + " " + "[" + (((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) + "]" + " " + "has been disabled" + "!"), "code"))})), "delete_after": 8, "allowed_mentions": None})






        if (passedPerms == True):

            if (function == None):
                message = message
            elif (function != None):

                dataToSend = await (eval("self" + "." + function))


                if ((dataToSend[1]) == "message"):
                    message = (dataToSend[0])

                elif ((dataToSend[1]) == "embed"):
                    embed = (dataToSend[0])

                try:

                    if ((dataToSend[3]) == None):
                        additionalSendOptions = False
                    elif ((dataToSend[3]) != None):
                        additionalSendOptions = True

                except Exception as exception:
                    additionalSendOptions = False









            if ((message == None) and (embed == None) and (file == None)):
                pass
            elif ((message != None) or (embed != None) or (file != None)):




                if (deleteMessages == True):
                    deleteTime = deleteTime
                elif (deleteMessages == False):
                    deleteTime = None

                if (embed == None):
                    embed = None
                if (embed != None):
                    await self.printOutputToLogs(embed, callingMessage)

                    if ((type(embed)) == tuple):
                        embed = self.createEmbed((embed[0]), (embed[1]))
                    elif ((type(embed)) != tuple):
                        embed = self.createEmbed(embed)



                    if (((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) == "?") or ((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) == "help")):
                        await self.sendMessage({"content": message, "embed": embed, "delete_after": deleteTime}, ["<:home:882810562126417930>", "<:restricted:882810562214518835>", "<:automated:915861328235757599>", "<:code:882810561690222613>", "<:symbols:882810561786699817>", "<:acknowledgements:882810562055131186>"])


                    elif (((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) != "?") and ((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) != "help")):
                        await self.sendMessage({"content": message, "embed": embed, "delete_after": deleteTime})





                elif (message != None):

                    if (len(message) < 2000):
                        
                        if (additionalSendOptions == True):
                            await self.sendMessage({"content": message, "delete_after": deleteTime, "reference": (dataToSend[3][0]), "mention_author": (dataToSend[3][1])})
                        elif (additionalSendOptions == False):
                            await self.sendMessage({"content": message, "delete_after": deleteTime})


                    elif (len(message) >= 2000):

                        if ((((bool(re.search("^```.{0,24}\n", (message[0:32]))))) == True) and ((bool(re.search("```$", (message[-8:])))) == True)):
                            extension = (message[(((re.search("^```.{0,24}\n", (message[0:32]))).start()) + 3):(((re.search("^```.{0,24}\n", (message[0:32]))).end()) - 1)])
                            message = message[((re.search("^```.{0,24}\n", (message[0:32]))).end()):(((re.search("```$", (message[-8:]))).start()) - 8)]
                            tempFile = io.BytesIO(message.encode())
                            discordFile = (discord.File(tempFile, ("message" + "." + extension)))
                        elif ((((bool(re.search("^```.{0,24}\n", (message[0:32]))))) == False) or ((bool(re.search("```$", (message[-8:])))) == False)):
                            tempFile = io.BytesIO(message.encode())
                            discordFile = (discord.File(tempFile, "message.txt"))

                        await self.sendMessage({"file": discordFile, "delete_after": deleteTime})






        elif (passedPerms == False):
            print(callingMessage)








    async def on_ready(self):

        global botItself
        global botMaster
        global botLogger
        # global botSecondaryLogger
        global virtualParameters
        global connectedVoiceChannels

        botItself = await client.fetch_user(self.user.id)
        botMaster = await client.fetch_user(master)
        botLogger = await client.fetch_channel(logChannel)
        # botSecondaryLogger = await client.fetch_channel(887489153418289202)
        connectedVoiceChannels = []

        await self.addListeners()

        await self.printOutputToLogs("Logged in as " + "'" + (str(self.user.name)) + "'" + " (" + (str(self.user.id)) + ")")

        # virtualParameters = defaultStatus
        # await self.setStatus()



        async def changeStatusLoop():
            await self.changeStatus()

        
        changeStatusLoop = (discord.ext.tasks.loop(minutes = 120)(changeStatusLoop))
        changeStatusLoop.start()



        """


        countingChannel = await client.fetch_channel(882058561377673228)
        baseCount = (int((await ((countingChannel.history(limit = 1)).flatten()))[0]))
        maximumCount = 10
        repeats = 0
        while (repeats < maximumCount):
            await countingChannel.send(str(baseCount + repeats))
            repeats = repeats + 1


        """






    async def on_message(self, message):

        if ((message.author.id) == (self.user.id)):
            pass

        elif ((message.author.id) != (self.user.id)):

            if ((message.author.bot) == True):
                pass



            elif ((message.author.bot) == False):




                global callingMessage
                messageContent = message.content




                if ((len(message.mentions)) > 0):

                    if ((message.guild.id) in pingListeningGuilds):

                        callingMessage = message
                        messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                        messageMentions = ""


                        repeats = 0
                        while (repeats < (len(message.mentions))):
                            messageMentions = messageMentions + (((message.mentions)[repeats]).mention) + ", "
                            repeats = repeats + 1


                        messageMentions = messageMentions[0:-2]

                        await messageGuildLogChannel.send((((message.author).mention) + "\n" + (format("mentioned", "bold")) + "\t" + messageMentions + "\n" + (format("in", "bold")) + "\t\t\t\t\t" + ((message.channel).mention) + "\n" + (format("at", "bold")) + "\t\t\t\t\t" + (("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "d" + ">")) + " " + ("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "T" + ">")) + " " + "(" + (format((str(((message.created_at).timestamp()) - timeOffset)), "code")) + ")") + "\n" + (format("with", "bold")) + "\n" + (format((message.content), ["quote", "cBlock"]))), allowed_mentions = (discord.AllowedMentions(users = False)))




                if ((len(message.role_mentions)) > 0):

                    if ((message.guild.id) in pingListeningGuilds):

                        callingMessage = message
                        messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])

                        messageMentions = ""


                        repeats = 0
                        while (repeats < (len(message.role_mentions))):
                            messageMentions = messageMentions + (((message.role_mentions)[repeats]).mention) + ", "
                            repeats = repeats + 1


                        messageMentions = messageMentions[0:-2]



                        await messageGuildLogChannel.send((((message.author).mention) + "\n" + (format("mentioned", "bold")) + "\t" + messageMentions + "\n" + (format("in", "bold")) + "\t\t\t\t\t" + ((message.channel).mention) + "\n" + (format("at", "bold")) + "\t\t\t\t\t" + (("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "d" + ">")) + " " + ("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "T" + ">")) + " " + "(" + (format((str(((message.created_at).timestamp()) - timeOffset)), "code")) + ")") + "\n" + (format("with", "bold")) + "\n" + (format((message.content), ["quote", "cBlock"]))), allowed_mentions = (discord.AllowedMentions(users = False)))





                if ((bool(re.match("^register mentions logging to {0,2}<#\d{1,20}> {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()
                        # messageContent = "register mentions logging to <#456>"
                        extractedMessage = []
                        splitMessageContent = (messageContent.split("register mentions logging to", 1))
                        extractedMessage.append(splitMessageContent[1])
                        print(extractedMessage)


                        try:

                            newMentionsLogsChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[0])))[0])
                            newMentionsLogsChannelId = (int((re.findall("\d{1,20}", newMentionsLogsChannel))[0]))

                            if (((message.guild.id) in pingListeningGuilds) == True):
                                await self.sendMessage({"content": "mention logging already exists in this guild\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif (((message.guild.id) in pingListeningGuilds) == False):

                                newMentionData = [(message.guild.id), newMentionsLogsChannelId]
                                await self.addMentionListener(newMentionData)

                                await self.sendMessage({"content": "mention logging activated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                        except Exception as exception:
                            await self.sendMessage({"content": "syntax error\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})



                    elif ((message.author.id) not in authorisedUsers):
                        pass






                if ((bool(re.match("^unregister mentions logging$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()


                        mentionDataPosition = pingListeningGuilds.index(message.guild.id)

                        if ((mentionDataPosition >= 0) and (mentionDataPosition <= (len(pingListeningGuilds)))):
                            await self.removeMentionListener(mentionDataPosition)
                            await self.sendMessage({"content": "mention logging deactivated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif ((mentionDataPosition < 0) or (mentionDataPosition > (len(pingListeningGuilds)))):
                            await self.sendMessage({"content": "mention logging deactivation failed\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                    elif ((message.author.id) not in authorisedUsers):
                        pass











                if ((bool(re.match("^create role .{0,32}, ?#[0-9A-Fa-f]{6}$", messageContent))) == True):

                    if ((message.channel.id) in roleListeningChannels):

                        if (commandsEnabled == True):

                            callingMessage = message

                            await message.channel.trigger_typing()

                            newRole = await (message.guild).create_role(name = (messageContent[12:-9]), color = (int((messageContent[-6:]), 16)), reason = ("user" + " " + " " + " " + "requested"))
                            await newRole.edit(position = (((message.guild.get_role(roleListeningChannelsPosition[(message.channel.id)])).position) - 1))
                            await message.author.add_roles(newRole, reason = ("user" + " " + " " + " " + "requested"))
                            await self.sendMessage({"content": ("role" + " " + (newRole.mention) + " " + "created by" + " " + ((message.author).mention)), "embed": None, "delete_after": None, "allowed_mentions": None})
                            await self.addRoleListener((message.channel.id), (newRole.id))


                        elif (commandsEnabled == False):
                            pass



                elif ((bool(re.match("^create role .{0,32}, ?#[0-9A-Fa-f]{6}$", messageContent))) == False):
                    pass










                if ((bool(re.match("^assign role <@&!?\d{1,20}>$", messageContent))) == True):

                    if ((message.channel.id) in roleListeningChannels):

                        if (commandsEnabled == True):

                            callingMessage = message

                            await message.channel.trigger_typing()

                            if ((message.raw_role_mentions)[0]) in (roleListeningChannelsRoles[(message.channel.id)]):

                                await message.author.add_roles(((message.role_mentions)[0]), reason = ("user" + " " + " " + " " + "requested"))
                                await self.sendMessage({"content": ("role" + " " + (((message.role_mentions)[0]).mention) + " " + "assigned by" + " " + ((message.author).mention)), "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif ((message.raw_role_mentions)[0]) not in (roleListeningChannelsRoles[(message.channel.id)]):

                                await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`role requested is not a custom role`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif (commandsEnabled == False):
                            pass



                elif ((bool(re.match("^assign role <@&!?\d{1,20}>$", messageContent))) == False):
                    pass














                if ((bool(re.match("^rep /.{0,256}/, \d{1,20}$", messageContent))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()


                        regexToMatch = ((messageContent[((re.search("^rep ", messageContent)).end()):((re.search(", \d{1,20}$", messageContent)).start())])[1:-1])
                        messagesToSearch = (int(messageContent[((re.search("\d{1,20}$", messageContent)).start()):]))



                        if ((messagesToSearch >= 0) and (messagesToSearch <= 128)):
                            pass
                        elif (messagesToSearch < 0):
                            await self.sendMessage({"content": "the number of messages requested is out of the acceptable range\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                        elif (messagesToSearch > 128):
                            await self.sendMessage({"content": "the number of messages requested is out of the acceptable range\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})



                        channelMessages = (await (((message.channel).history(limit = messagesToSearch)).flatten()))


                        messagesToDelete = []
                        messagesToDeleteDescriptions = []

                        try:

                            repeats = 0
                            while (repeats < (len(channelMessages))):

                                print(((channelMessages[repeats]).content))

                                if ((bool(re.search(regexToMatch, ((channelMessages[repeats]).content)))) == True):
                                    messagesToDelete.append(channelMessages[repeats])
                                    messagesToDeleteDescriptions.append((channelMessages[repeats]).content)

                                elif ((bool(re.search(regexToMatch, ((channelMessages[repeats]).content)))) == False):
                                    pass

                                repeats = repeats + 1


                        except Exception as exception:
                            await self.sendMessage({"content": "regex parsing error" + "\n" + "||`" + (str(exception) + "`||"), "embed": None, "delete_after": None, "allowed_mentions": None})



                            repeats = repeats + 1



                        print(messagesToDelete)


                        await self.sendMessage({"content": ("ready to delete" + "\n" + ((json_dumps(messagesToDeleteDescriptions, separators = (",\n", ":\n")))[0:1792])), "embed": None, "delete_after": None, "allowed_mentions": None})


                    elif ((message.author.id) not in authorisedUsers):
                        pass










                # verificationListeningChannels = []
                # verificationListeningChannelsLogs = {}
                # verificationListeningChannelsRoles = {}
                # verificationListeningChannelsRequiredRoles = {}



                # messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.guild.id)])
                # await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))



                if ((bool(re.match("^i verify <@!?\d{1,20}>$", (messageContent.lower())))) == True):

                    if ((message.channel.id) in verificationListeningChannels):



                        callingMessage = message

                        await message.channel.trigger_typing()



                        if ((message.author.id) in authorisedUsers):

                            rolesToAddIds = (verificationListeningChannelsRoles[(message.channel.id)])
                            rolesToAdd = []

                            repeats = 0
                            while (repeats < (len(rolesToAddIds))):
                                rolesToAdd.append(message.guild.get_role(rolesToAddIds[repeats]))
                                repeats = repeats + 1

                            print(rolesToAdd)

                            await ((message.mentions)[0]).add_roles(*rolesToAdd)
                            await self.sendMessage({"content": None, "embed": (self.createEmbed("userVerified", {"description": ("verified user" + " " + (((message.mentions)[0]).name) + "#" + (((message.mentions)[0]).discriminator))})), "delete_after": None, "allowed_mentions": None})

                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                            await messageGuildLogChannel.send(("\u2705" + " " + ((message.author).mention) + " " + "verified" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))





                        elif ((message.author.id) not in authorisedUsers):






                            if (commandsEnabled == True):



                                requiredRoles = (verificationListeningChannelsRequiredRoles[(message.channel.id)])
                                requiredRolesIds = []

                                repeats = 0
                                while (repeats < (len(requiredRoles))):
                                    requiredRolesIds.append(message.guild.get_role(requiredRoles[repeats]))
                                    repeats = repeats + 1



                                if ((len((set(message.author.roles)).intersection(set(requiredRolesIds)))) == 0):
                                    await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you must have 'nsbhs' to use this command)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                    messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                    await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                elif ((len((set(message.author.roles)).intersection(set(requiredRolesIds)))) != 0):

                                    if ((((message.mentions)[0]).bot) == True):
                                        await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you cannot verify non-humans)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                        messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                        await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                    elif ((((message.mentions)[0]).bot) == False):

                                        if ((len((set(((message.mentions)[0]).roles)).intersection(set(requiredRolesIds)))) == 0):

                                            rolesToAddIds = (verificationListeningChannelsRoles[(message.channel.id)])
                                            rolesToAdd = []

                                            repeats = 0
                                            while (repeats < (len(rolesToAddIds))):
                                                rolesToAdd.append(message.guild.get_role(rolesToAddIds[repeats]))
                                                repeats = repeats + 1


                                            await ((message.mentions)[0]).add_roles(*rolesToAdd)
                                            await self.sendMessage({"content": None, "embed": (self.createEmbed("userVerified", {"description": ("verified user" + " " + (((message.mentions)[0]).name) + "#" + (((message.mentions)[0]).discriminator))})), "delete_after": None, "allowed_mentions": None})
                                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                            await messageGuildLogChannel.send(("\u2705" + " " + ((message.author).mention) + " " + "verified" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                        elif ((len((set(((message.mentions)[0]).roles)).intersection(set(requiredRolesIds)))) != 0):
                                            await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you cannot verify already verified users)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                            await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))





                            elif (commandsEnabled == False):
                                pass








                if ((bool(re.match("^register verification in {0,2}<#\d{1,20}> {0,2}logging to {0,2}<#\d{1,20}> {0,2}requiring {0,2}(<@&!?\d{1,20}>,? ?){1,} {0,2}applying {0,2}(<@&!?\d{1,20}>,? ?){1,} {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):


                        callingMessage = message

                        await message.channel.trigger_typing()
                        # messageContent = "register verification in <#123> logging to <#456> requiring <@&789> applying <@&000>"
                        extractedMessage = []
                        splitMessageContent = (messageContent.split("register verification in", 1))
                        splitMessageContent = (splitMessageContent[1]).split("logging to", 1)
                        extractedMessage.append(splitMessageContent[0])
                        splitMessageContent = (splitMessageContent[1]).split("requiring", 1)
                        extractedMessage.append(splitMessageContent[0])
                        splitMessageContent = (splitMessageContent[1]).split("applying", 1)
                        extractedMessage.append(splitMessageContent[0])
                        extractedMessage.append(splitMessageContent[1])
                        print(extractedMessage)


                        try:
                            # newVerificationChannel = ((re.findall("\d{1,20}", (extractedMessage[0])))[0])
                            # newVerificationLogsChannel = ((re.findall("\d{1,20}", (extractedMessage[1])))[0])
                            # newVerificationRoles = (re.findall("\d{1,20}", (extractedMessage[2])))
                            # newVerificationAppliedRoles = (re.findall("\d{1,20}", (extractedMessage[3])))

                            newVerificationChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[0])))[0])
                            newVerificationLogsChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[1])))[0])
                            newVerificationRoles = (re.findall("<@&!?\d{0,20}>", (extractedMessage[2])))
                            newVerificationAppliedRoles = (re.findall("<@&!?\d{0,20}>", (extractedMessage[3])))

                            newVerificationChannelId = (int((re.findall("\d{1,20}", newVerificationChannel))[0]))
                            newVerificationLogsChannelId = (int((re.findall("\d{1,20}", newVerificationLogsChannel))[0]))
                            newVerificationRolesIds = []
                            newVerificationAppliedRolesIds = []

                            repeats = 0
                            while (repeats < (len(newVerificationRoles))):
                                newVerificationRolesIds.append(int((re.findall("\d{1,20}", (newVerificationRoles[repeats])))[0]))
                                repeats = repeats + 1

                            repeats = 0
                            while (repeats < (len(newVerificationAppliedRoles))):
                                newVerificationAppliedRolesIds.append(int((re.findall("\d{1,20}", (newVerificationAppliedRoles[repeats])))[0]))
                                repeats = repeats + 1



                            if ((newVerificationChannel in verificationListeningChannels) == True):
                                await self.sendMessage({"content": "verification already exists for the specified channel\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif ((newVerificationChannel in verificationListeningChannels) == False):

                                newVerificationData = [newVerificationChannelId, newVerificationLogsChannelId, newVerificationRolesIds, newVerificationAppliedRolesIds]
                                await self.addVerificationListener(newVerificationData)

                                await self.sendMessage({"content": "verification activated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                        except Exception as exception:
                            await self.sendMessage({"content": "syntax error\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})




                    elif ((message.author.id) not in authorisedUsers):
                        pass



                if ((bool(re.match("^unregister verification in {0,2}<#\d{1,20}> {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):

                        callingMessage = message

                        await message.channel.trigger_typing()

                        verificationDataPosition = verificationListeningChannels.index(((message.channel_mentions)[0]).id)

                        if ((verificationDataPosition >= 0) and (verificationDataPosition <= (len(verificationListeningChannels)))):
                            await self.removeVerificationListener(verificationDataPosition)
                            await self.sendMessage({"content": "verification deactivated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif ((verificationDataPosition < 0) or (verificationDataPosition > (len(verificationListeningChannels)))):
                            await self.sendMessage({"content": "verification deactivation failed\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})






                if ((messageContent.startswith("\\")) == True):

                    command = ((((messageContent[1:]).split(" ", 1))[0]).lower())




                    if (command in (validCommands["commands"])):

                        await message.channel.trigger_typing()

                        await self.createMessage(originalMessage = message, **(validCommands["preReplies"][(validCommands["replies"][command])]))


                elif ((messageContent.startswith("\\")) == False):
                    pass




                if (botItself in (message.mentions)):



                    if ((bool(re.match("^ {0,2}<@!?\d{1,20}> {0,2}$", (messageContent.lower())))) == True):


                        if (commandsEnabled == True):

                            callingMessage = message
                            await message.channel.trigger_typing()

                            await self.sendMessage({"content": "*did you mean to use* \u2009`\\?` *?*", "embed": None, "delete_after": 4, "allowed_mentions": None})

                        elif (commandsEnabled == False):
                            pass








        else:
            await self.printOutputToLogs("Something went seriously wrong at \'MyClient\\on_message\'")





    async def on_reaction_add(self, reaction, user):



        if (reactionsEnabled == True):


            if (commandsEnabled == True):




                if ((user.id) == (self.user.id)):
                    pass

                elif ((user.id) != (self.user.id)):

                    reactions = {
                        "<:home:882810562126417930>": "helpMenu",
                        "<:restricted:882810562214518835>": "restrictedHelpMenu",
                        "<:automated:915861328235757599>": "automatedHelpMenu",
                        "<:code:882810561690222613>": "iteratorHelpMenu",
                        "<:symbols:882810561786699817>": "symbolKeyHelpEmbed",
                        "<:acknowledgements:882810562055131186>": "acknowledgementsHelpEmbed",
                    }

                    reactionNames = list(reactions.keys())



                    reactedMessage = (reaction.message)

                    if ((reactedMessage.author.id) == (self.user.id)):



                        if ((str(reaction.emoji)) in reactionNames):


                            emojiUser = await client.fetch_user(user.id)

                            embed = self.createEmbed(reactions[str(reaction.emoji)])


                            await reactedMessage.remove_reaction((reaction.emoji), emojiUser)
                            await reactedMessage.edit(content = None, embed = embed, allowed_mentions = (discord.AllowedMentions(everyone = False, users = False, roles = False, replied_user = False)))


                        elif ((str(reaction.emoji)) == "\U0001F9D0"):

                            messageReactions = ((reaction.message).reactions)
                            print(messageReactions)

                            if ((((messageReactions[((len(messageReactions)) - 1)]).emoji) == "\U0001F9D0") and (((messageReactions[((len(messageReactions)) - 2)]).emoji) == "\U0001FA84")):

                                emojiUser = await client.fetch_user(user.id)

                                await (reaction.message).remove_reaction((messageReactions[((len(messageReactions)) - 1)]), emojiUser)
                                await (reaction.message).remove_reaction((messageReactions[((len(messageReactions)) - 2)]), emojiUser)

                                embed = self.createEmbed("undocumentedHelpMenu")

                                await (reaction.message).edit(content = None, embed = embed, allowed_mentions = (discord.AllowedMentions(everyone = False, users = False, roles = False, replied_user = False)))













                    elif ((reactedMessage.author.id) != (self.user.id)):
                        pass








            elif (commandsEnabled == False):
                pass




        elif (reactionsEnabled == False):
            pass





































readSettings()








generateDiscordClasses()


generateEmbeds()






recalculateCommands()



client = MyClient()
client.run(token)



input("Press enter to close")
